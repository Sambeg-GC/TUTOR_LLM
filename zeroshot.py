"""
AI-Powered Academic Tutor
Step 2: Zero-Shot Prompting

Zero-shot = we give the model an instruction only, no example answers
to copy the style/format from. Demonstrates three academic use cases:
  1. Explain a topic
  2. Summarize study material
  3. Simplify a complex concept

Run:
  python step2_zero_shot.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession


MENU = """
============================================================
AI Academic Tutor — Step 2: Zero-Shot Prompting
============================================================
1. Explain a topic
2. Summarize study material
3. Simplify a complex concept
4. View conversation history
5. Exit
"""


def main():
    llm = get_llm()
    session = TutorSession(llm)

    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            topic = input("Topic to explain: ").strip()
            if topic:
                print(f"\nTutor:\n{session.explain(topic)}")

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
                print(f"\nTutor:\n{session.summarize(material)}")

        elif choice == "3":
            concept = input("Concept to simplify: ").strip()
            if concept:
                print(f"\nTutor:\n{session.simplify(concept)}")

        elif choice == "4":
            session.show_history()

        elif choice == "5":
            print("Goodbye! Keep studying.")
            break

        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()