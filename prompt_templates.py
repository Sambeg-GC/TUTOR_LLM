"""
AI-Powered Academic Tutor
Step 6: Prompt Templates

Run:
  python prompt_templates.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession

def main():
    llm = get_llm()
    session = TutorSession(llm)

    while True:
        print("\n" + "=" * 60)
        print("AI Academic Tutor — Step 6: Prompt Templates")
        print("=" * 60)
        print("1. Generate custom Study Guide")
        print("2. View conversation history")
        print("3. Exit")
        print("=" * 60)

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            topic = input("Enter the main topic (e.g., Photosynthesis): ").strip()
            focus_area = input("Enter the specific focus area (e.g., The Light Reactions): ").strip()
            
            if topic and focus_area:
                print("\n[System] Generating study guide...")
                guide = session.generate_study_guide(topic, focus_area)
                print(f"\nTutor:\n{guide}")
                
        elif choice == "2":
            session.show_history()
            
        elif choice == "3":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()