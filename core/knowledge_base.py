"""
Shared Knowledge Base for the AI Academic Tutor project.
Adds Retrieval-Augmented Generation (RAG): grounds the tutor's answers in
the student's own uploaded material (PDFs, notes, textbooks) instead of
relying purely on the model's training data.
"""

import os
import re
import time
import glob
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# Free-tier embed_content quota is 100 requests/minute. Keep batches small
# and pace them so a big folder doesn't blow through that in a few seconds.
EMBED_BATCH_SIZE = 20
PAUSE_BETWEEN_BATCHES = 5  # seconds
MAX_RETRIES = 5


class KnowledgeBase:
    def __init__(self, persist_dir: str = "vector_store"):
        self.persist_dir = persist_dir
        self.embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
        )
        self.store = self._load_if_exists()

    def _load_if_exists(self):
        index_file = os.path.join(self.persist_dir, "index.faiss")
        if os.path.exists(index_file):
            print(f"\n[KB] Loading existing knowledge base from '{self.persist_dir}'...")
            return FAISS.load_local(
                self.persist_dir,
                self.embeddings,
                allow_dangerous_deserialization=True,
            )
        return None

    def _load_documents(self, path: str):
        """Loads a single file, or every supported file in a folder."""
        paths = [path]
        if os.path.isdir(path):
            paths = glob.glob(os.path.join(path, "**", "*.*"), recursive=True)

        docs = []
        for p in paths:
            ext = os.path.splitext(p)[1].lower()
            try:
                if ext == ".pdf":
                    docs.extend(PyPDFLoader(p).load())
                elif ext in (".txt", ".md"):
                    docs.extend(TextLoader(p, encoding="utf-8").load())
                else:
                    continue  # skip unsupported file types
            except Exception as e:
                print(f"[KB] Skipped '{p}': {e}")
        return docs

    @staticmethod
    def _extract_retry_delay(exc) -> float | None:
        """Pulls Google's suggested retryDelay (seconds) out of a 429 error, if present."""
        match = re.search(r"retryDelay['\"]?\s*:\s*['\"](\d+)", str(exc))
        return float(match.group(1)) if match else None

    def _embed_batch_with_retry(self, batch):
        """Embeds one small batch, retrying with backoff if the free-tier
        rate limit (429 RESOURCE_EXHAUSTED) is hit."""
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                if self.store is None:
                    self.store = FAISS.from_documents(batch, self.embeddings)
                else:
                    self.store.add_documents(batch)
                return
            except Exception as e:
                if "RESOURCE_EXHAUSTED" not in str(e) and "429" not in str(e):
                    raise  # not a rate-limit error, don't swallow it
                wait = self._extract_retry_delay(e) or (10 * attempt)
                print(f"[KB]   rate-limited, waiting {wait:.0f}s before retry "
                      f"({attempt}/{MAX_RETRIES})...")
                time.sleep(wait)
        raise RuntimeError("Embedding failed after repeated rate-limit retries.")

    def ingest(self, path: str) -> int:
        """Loads, splits, embeds, and indexes a file or folder of study material.
        Returns the number of chunks added."""
        raw_docs = self._load_documents(path)
        if not raw_docs:
            print(f"[KB] No readable documents found at '{path}' (supported: .pdf, .txt, .md)")
            return 0

        chunks = self.splitter.split_documents(raw_docs)
        total = len(chunks)
        print(f"[KB] Split into {total} chunks. Embedding in batches of "
              f"{EMBED_BATCH_SIZE} to stay under the free-tier rate limit "
              f"(this may take a while for a large folder)...")

        for i in range(0, total, EMBED_BATCH_SIZE):
            batch = chunks[i:i + EMBED_BATCH_SIZE]
            self._embed_batch_with_retry(batch)
            done = min(i + EMBED_BATCH_SIZE, total)
            print(f"[KB]   embedded {done}/{total} chunks")
            if done < total:
                time.sleep(PAUSE_BETWEEN_BATCHES)

        os.makedirs(self.persist_dir, exist_ok=True)
        self.store.save_local(self.persist_dir)

        print(f"[KB] Indexed {total} chunks from '{path}'.")
        return total

    def retrieve(self, query: str, k: int = 4):
        """Returns the top-k most relevant chunks as (text, source) pairs."""
        if self.store is None:
            return []
        results = self.store.similarity_search(query, k=k)
        return [(doc.page_content, doc.metadata.get("source", "unknown")) for doc in results]