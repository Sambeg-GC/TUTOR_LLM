"""
AI-Powered Academic Tutor
Step 8: Memory System (Clean Production Version)

Run:
  python memory_system.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession

def main():
    llm = get_llm()
    session = TutorSession(llm)
    
    # Automatically load past session context on boot
    session.load_history()

    while True:
        print("\n" + "=" * 60)
        print("AI Academic Tutor — Step 8: Memory System")
        print("=" * 60)
        print("1. Ask a question (Auto-saves context)")
        print("2. View full history")
        print("3. Clear all memory")
        print("4. Exit")
        print("=" * 60)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            user_input = input("\nYou: ").strip()
            if user_input:
                answer = session.ask(user_input)
                print(f"\nTutor: {answer}")
                session.save_history()
                
        elif choice == "2":
            session.show_history()
            
        elif choice == "3":
            import os
            if os.path.exists("tutor_history.json"):
                os.remove("tutor_history.json")
            # Reset history to empty (or keep system prompt if you prefer)
            session.history = []
            print("\n[System] Memory wiped completely!")
            
        elif choice == "4":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()