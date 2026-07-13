"""
AI-Powered Academic Tutor
Step 3: Few-Shot Prompting

Few-shot = the prompt includes one worked EXAMPLE of the desired output
format before asking the model to produce new content. This is what
makes quiz/notes formatting consistent across multiple runs, unlike
zero-shot (Step 2), where format can vary each time.

Run:
  python step3_few_shot.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession


MENU = """
============================================================
AI Academic Tutor — Step 3: Few-Shot Prompting
============================================================
1. Generate a quiz (consistent MCQ format)
2. Categorize study notes (Tagged format)
3. View conversation history
4. Exit
"""


def main():
    llm = get_llm()
    session = TutorSession(llm)

    while True:
        print(MENU)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            topic = input("Quiz topic: ").strip()
            num_str = input("Number of questions (default 3): ").strip()
            num_questions = int(num_str) if num_str.isdigit() else 3
            if topic:
                print(f"\nTutor:\n{session.generate_quiz(topic, num_questions)}")

        elif choice == "2":
            print("Paste the study material (end with an empty line):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            material = "\n".join(lines)
            if material:
                print(f"\nTutor:\n{session.categorize_notes(material)}")

        elif choice == "3":
            session.show_history()

        elif choice == "4":
            print("Goodbye! Keep studying.")
            break

        else:
            print("Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()