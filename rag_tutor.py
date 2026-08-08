"""
AI-Powered Academic Tutor
RAG Extension: Retrieval-Augmented Generation

Grounds answers in the student's own uploaded material (PDFs, notes,
.md/.txt files) instead of relying purely on the model's training data.

Run:
  python rag_tutor.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession
from core.knowledge_base import KnowledgeBase

def main():
    llm = get_llm()
    kb = KnowledgeBase(persist_dir="vector_store")
    session = TutorSession(llm, kb=kb)

    while True:
        print("\n" + "=" * 60)
        print("AI Academic Tutor — RAG Mode")
        print("=" * 60)
        print("1. Ingest study material (file or folder path)")
        print("2. Ask a question (answered from your materials)")
        print("3. View conversation history")
        print("4. Exit")
        print("=" * 60)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            path = input("Enter a file or folder path to ingest: ").strip()
            if path:
                kb.ingest(path)

        elif choice == "2":
            question = input("\nYou: ").strip()
            if question:
                answer = session.ask_with_rag(question)
                print(f"\nTutor: {answer}")

        elif choice == "3":
            session.show_history()

        elif choice == "4":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()