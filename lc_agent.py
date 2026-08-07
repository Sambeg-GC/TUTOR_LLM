"""
AI-Powered Academic Tutor
Step 9: Agents & Tools (Calculator + Summarizer + Study Planner)

Run:
  python lc_agent.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession

def main():
    llm = get_llm()

    user_name = input("Enter your name (keeps your history separate from other students): ").strip() or "Student"
    session = TutorSession(llm, user_id=user_name, user_name=user_name)

    # Reload this user's cross-session history automatically
    session.load_history()

    print("\n" + "=" * 60)
    print(f"AI Academic Tutor — Step 9: Agent & Custom Tools ({session.user_name})")
    print("=" * 60)
    print("The agent now picks between THREE real tools:")
    print("  - calculate          e.g. 'What is 4532 times 14, plus the square root of 81?'")
    print("  - summarize_text     e.g. 'Summarize this paragraph: <paste text>'")
    print("  - create_study_plan  e.g. 'Plan my study week for Biology and Chemistry, exam in 10 days'")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye! Keep studying.")
            break

        if user_input:
            print("\n[Agent Loop Started - Watch Tool Execution Below]")
            answer = session.ask_with_tools(user_input)
            print(f"\nTutor: {answer}")

if __name__ == "__main__":
    main()