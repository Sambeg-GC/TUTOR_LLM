"""
AI-Powered Academic Tutor
Step 9: Agents & Tools

Run:
  python lc_agent.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession

def main():
    llm = get_llm()
    session = TutorSession(llm)
    
    # Reload cross-session history automatically
    session.load_history()

    print("\n" + "=" * 60)
    print("AI Academic Tutor — Step 9: Agent & Custom Tools")
    print("=" * 60)
    print("Test me with a complex math question to see the tool fire!")
    print("Example: 'What is 4532 times 14 and what is the square root of that result?'")
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