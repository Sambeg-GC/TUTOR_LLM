"""
AI-Powered Academic Tutor
Step 1: LLM API Integration  (Gemini via LangChain)

Setup:
  pip install langchain-google-genai langchain langchain-core
  export GOOGLE_API_KEY="your-key-here"

Run:
  python step1_llm_integration.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession


def main():
    print("=" * 61)
    print("AI Academic Tutor — Step 1: LLM API Integration")
    print("Type 'history' to view the conversation log, 'exit' to quit.")
    print("=" * 60)

    llm = get_llm()
    session = TutorSession(llm)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye! Keep studying.")
            break
        if user_input.lower() == "history":
            session.show_history()
            continue
        if not user_input:
            continue

        try:
            answer = session.ask(user_input)
            print(f"\nTutor: {answer}")
        except Exception as e:
            print(f"\n[Error] {e}")


if __name__ == "__main__":
    main()