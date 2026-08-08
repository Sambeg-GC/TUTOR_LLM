# 🎓 Tutor_LLM | AI-Powered Academic Tutor

A console-based AI tutoring system built with **Python** and the **Google Gemini API**, exploring core prompt engineering techniques and LangChain-based application patterns—from a simple LLM call to autonomous agents capable of selecting and using tools, extended with a Retrieval-Augmented Generation (RAG) pipeline for grounding answers in a student's own study material.

This project is designed as a **structured lab project**, where each step introduces one new concept while preserving all previous functionality. A single shared `TutorSession` class evolves throughout the project, demonstrating incremental software development and modular design.

---

# ✨ Features

| Status | Feature | File |
|:------:|---------|------|
| ✅ | Session-based conversation with full context history | `llm_integration.py` |
| ✅ | Zero-shot prompting (explain, summarize, simplify) | `zeroshot.py` |
| ✅ | Few-shot prompting (quiz generation, structured notes) | `fewshot.py` |
| ✅ | Chain-of-Thought prompting (step-by-step problem solving) | `chain_of_thought.py` |
| ✅ | Role prompting (Teacher, Examiner, Coach, Subject Expert) | `role_prompting.py` |
| ✅ | Reusable prompt templates with dynamic input substitution | `prompt_templates.py` |
| ✅ | LangChain chains (Topic → Explanation → Notes → Quiz pipeline) | `lc_chains.py` |
| ✅ | Memory system (persist per-user identity and learning history) | `memory_system.py` |
| ✅ | Agents & tools (calculator, study planner, summarizer — 3 real, independently-selectable LangChain tools) | `lc_agent.py` |
| ✅ | Final integrated console application | `main_app.py` |
| ✅ | Retrieval-Augmented Generation — ingest study material (PDF/TXT/MD), answer grounded in sources with citations (standalone console, not yet merged into `main_app.py`) | `rag_tutor.py`, `core/knowledge_base.py` |

---

# 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini API**
  - Chat: `gemini-2.5-flash`
  - Embeddings: `gemini-embedding-001`
- **LangChain**
  - `langchain`
  - `langchain-core`
  - `langchain-google-genai`
  - `langchain-community` (document loaders, FAISS integration)
  - `langchain-text-splitters` (chunking for RAG)
- **FAISS** (`faiss-cpu`) — local vector store for RAG
- **pypdf** — PDF parsing for RAG ingestion
- **python-dotenv** for environment variable management
- **Retry & Error Handling**
  - `.with_retry()` for transient chat-API failures
  - Custom 45-second backoff mechanism for Gemini rate limits
  - Batched, rate-limited embedding with automatic retry/backoff for RAG ingestion

---

# 📁 Project Structure

```text
Tutor_LLM/
│
├── .env                      # API key
├── .gitignore                # excludes vector_store/, tutor_history*.json, .env
├── requirements.txt          # pinned dependencies
│
├── core/                     # Shared engine
│   ├── __init__.py
│   ├── llm_setup.py          # Gemini client & model configuration
│   ├── tutor_session.py      # Shared TutorSession class
│   └── knowledge_base.py     # KnowledgeBase class — chunking, embedding, FAISS retrieval (RAG)
│
├── llm_integration.py        # Step 1
├── zeroshot.py               # Step 2
├── fewshot.py                # Step 3
├── chain_of_thought.py       # Step 4
├── role_prompting.py         # Step 5
├── prompt_templates.py       # Step 6
├── lc_chains.py               # Step 7
├── memory_system.py           # Step 8
├── lc_agent.py                 # Step 9
├── main_app.py                  # Step 10
├── rag_tutor.py                  # Step 11 (extension) — RAG console
└── vector_store/                  # auto-generated FAISS index (gitignored)
```

> **Architecture Principle**
>
> The `core/` package contains the reusable engine shared across every step. Each step file is independently executable while importing shared functionality from `core/`, ensuring new features never break previous implementations. `rag_tutor.py` follows the same pattern: it's a standalone entrypoint that reuses `TutorSession` and adds a `KnowledgeBase`, without modifying how `main_app.py` or the earlier step files behave.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Tutor_LLM.git
cd Tutor_LLM
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure the API Key

Copy the environment template:

```bash
cp .env.example .env
```

Edit the `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

You can obtain a free API key from **Google AI Studio**. Note that the free tier's `embed_content` quota (100 requests/minute) applies to RAG ingestion — large folders may take a few minutes as `KnowledgeBase.ingest()` paces itself under that limit.

---

## 5. Run the Application

```bash
python main_app.py      # unified console: chains, memory, agent tools (Steps 7–10)
python rag_tutor.py     # standalone RAG console: ingest study material + ask (Step 11)
```

---

# 📦 Requirements

```text
langchain
langchain-core
langchain-google-genai
langchain-community
langchain-text-splitters
python-dotenv
faiss-cpu
pypdf
```

Or install directly:

```bash
pip install langchain langchain-core langchain-google-genai langchain-community langchain-text-splitters python-dotenv faiss-cpu pypdf
```

---

# 🗺️ Step-by-Step Learning Roadmap

| Step | Topic | Concept Introduced | Status |
|------:|-------|-------------------|:------:|
| 1 | LLM API Integration | Connect to Gemini, maintain session history | ✅ |
| 2 | Zero-Shot Prompting | Instruction-only prompting | ✅ |
| 3 | Few-Shot Prompting | Example-guided output formatting | ✅ |
| 4 | Chain-of-Thought | Step-by-step reasoning | ✅ |
| 5 | Role Prompting | Persona-based prompting | ✅ |
| 6 | Prompt Templates | Reusable LangChain templates | ✅ |
| 7 | LangChain Chains | Sequential multi-step workflows (Topic → Explanation → Notes → Quiz) | ✅ |
| 8 | Memory System | Persistent, per-user conversation context | ✅ |
| 9 | Agents & Tools | ReAct agent selecting between 3 real tools | ✅ |
| 10 | Final Integration | Unified production-ready console application | ✅ |
| 11 | Retrieval-Augmented Generation | Ground answers in the student's own uploaded material via vector search | ✅ (standalone console) |

---

# ✅ Extension — Retrieval-Augmented Generation (RAG)

RAG has been implemented as **Step 11**, built on top of the concepts from Chains, Memory, and Agents.

**What it does:**

- 📚 Local **FAISS** vector store (persisted to `vector_store/`)
- 🧠 **Gemini embeddings** (`gemini-embedding-001`) for semantic search
- 📄 Ingests `.pdf`, `.txt`, and `.md` files — single files or whole folders (recursively)
- 🔍 Retrieves the top-k most relevant chunks for a question and answers **grounded only in that context**, citing source filenames, with an honest "not found in your materials" fallback instead of guessing
- ⏳ Embeds in small, rate-limited batches with automatic retry/backoff, to stay within the free-tier `embed_content` quota (100 requests/minute) on large ingests

**How to use it:**

```bash
python rag_tutor.py
```
1. Choose `1` and enter a file or folder path (absolute paths work regardless of your current directory)
2. Choose `2` and ask a question — answers cite which source file they came from
3. Re-running the script later reuses the existing `vector_store/` index instead of re-embedding everything

**Not yet done:**

- Not merged into `main_app.py`'s unified console — currently a separate entrypoint
- No formal RAG evaluation yet (Faithfulness / Answer Relevancy / Context Precision via RAGAS)
- No de-duplication if the same document is ingested twice

---

# 🐛 Known Issues & Fixes

| Issue | Cause | Solution |
|-------|-------|----------|
| **503 UNAVAILABLE** | Temporary Gemini server overload | Automatic retry with exponential backoff |
| **429 RESOURCE_EXHAUSTED** (chat) | Free-tier token/rate limit exceeded | `main_app.py` pauses for 45 seconds before retrying |
| **429 RESOURCE_EXHAUSTED** (RAG ingest) | Free-tier `embed_content` quota (100 req/min) exceeded when embedding many chunks from a large folder at once | `KnowledgeBase.ingest()` embeds in small batches with pacing and automatic retry/backoff |
| `Response prints as [{'type': 'text', ...}]` | Gemini returns content blocks instead of plain text | `_extract_text()` normalizes all response formats |
| `ModuleNotFoundError: core` | Running scripts from the wrong directory | Execute commands from the project root (`Tutor_LLM/`) |
| RAG ingest reports "No readable documents found" for a path that exists | Path pasted with surrounding quotes or duplicated (common with terminal auto-complete on folders with spaces) | Enter the raw path with no quotes; verify first with `Test-Path "<path>"` (PowerShell) |

---

# 📖 Learning Objectives

By completing this project, you will understand:

- Prompt Engineering fundamentals
- Zero-shot & Few-shot prompting
- Chain-of-Thought prompting
- Role-based prompting
- Prompt templating
- LangChain pipelines
- Memory systems and per-user state
- AI agents and tool calling (multi-tool selection)
- Retrieval-Augmented Generation: chunking, embeddings, vector search, grounded answering
- Error handling for production LLM applications, including API rate limits
- Incremental software architecture

---

# 👤 Author

**Sambeg G.C.**

---

# 📄 License

This project is intended for **educational and learning purposes**.