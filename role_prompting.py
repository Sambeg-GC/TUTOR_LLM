"""
AI-Powered Academic Tutor
Step 5: Role Prompting (Mid-Conversation Switching)

Run:
  python role_prompting.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession

def run_chat_loop(session, role_id, role_name):
    """Runs the chat loop and allows mid-conversation persona changes."""
    # First entry from main menu resets history for a clean start
    session.set_role(role_id, keep_history=False)
    
    # Map for mid-chat switching
    role_map = {
        "1": ("teacher", "Patient Teacher"),
        "2": ("examiner", "Strict Examiner"),
        "3": ("coach", "Study Coach"),
        "4": ("expert", "Subject Expert"),
        "5": ("default", "Default Tutor")
    }

    print(f"\n--- Chatting with {role_name} ---")
    print("Commands: 'back' to exit menu | '/switch' to change persona mid-chat")
    
    while True:
        user_input = input(f"\nYou [{role_name}]: ").strip()
        
        if user_input.lower() == "back":
            break
            
        if not user_input:
            continue
            
        # Handle mid-conversation switching
        if user_input.lower() == "/switch":
            print("\nSwitch Persona Mid-Chat:")
            print("1. Patient Teacher | 2. Strict Examiner | 3. Study Coach | 4. Subject Expert | 5. Default Tutor")
            choice = input("Choose (1-5): ").strip()
            
            if choice in role_map:
                role_id, role_name = role_map[choice]
                # Switch the persona but KEEP the history
                session.set_role(role_id, keep_history=True)
                print(f"\n[System] Persona swapped! You are now talking to the {role_name}.")
            else:
                print("\n[System] Invalid choice. Persona not changed.")
            continue
        
        answer = session.ask(user_input)
        print(f"\nTutor ({role_name}): {answer}")

def main():
    llm = get_llm()
    session = TutorSession(llm)

    while True:
        print("\n" + "=" * 60)
        print("AI Academic Tutor — Step 5: Role Prompting")
        print("=" * 60)
        print("1. Chat with Patient Teacher")
        print("2. Chat with Strict Examiner")
        print("3. Chat with Study Coach")
        print("4. Chat with Subject Expert")
        print("5. Chat with Default Tutor")
        print("6. View conversation history")
        print("7. Exit")
        print("=" * 60)

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            run_chat_loop(session, "teacher", "Patient Teacher")
        elif choice == "2":
            run_chat_loop(session, "examiner", "Strict Examiner")
        elif choice == "3":
            run_chat_loop(session, "coach", "Study Coach")
        elif choice == "4":
            run_chat_loop(session, "expert", "Subject Expert")
        elif choice == "5":
            run_chat_loop(session, "default", "Default Tutor")
        elif choice == "6":
            session.show_history()
        elif choice == "7":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()