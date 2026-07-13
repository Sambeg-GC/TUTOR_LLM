"""
AI-Powered Academic Tutor
Step 4: Chain-of-Thought Prompting

Chain-of-Thought = the model is explicitly instructed to reason through
intermediate steps before giving a final answer, instead of jumping
straight to a result. Useful for math, logic, and multi-part academic
problems where showing work matters as much as the answer.

Run:
  python step4_chain_of_thought.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession


MENU = """
============================================================
AI Academic Tutor — Step 4: Chain-of-Thought Prompting
============================================================
1. Solve a problem step-by-step
2. View conversation history
3. Exit
"""


def main():
    llm = get_llm()
    session = TutorSession(llm)

    while True:
        print(MENU)
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            problem = input("Enter the problem to solve: ").strip()
            if problem:
                print(f"\nTutor:\n{session.solve_step_by_step(problem)}")

        elif choice == "2":
            session.show_history()

        elif choice == "3":
            print("Goodbye! Keep studying.")
            break

        else:
            print("Please choose a number from 1 to 3.")


if __name__ == "__main__":
    main()