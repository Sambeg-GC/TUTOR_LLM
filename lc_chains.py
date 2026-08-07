"""
AI-Powered Academic Tutor
Step 7: LangChain Chains (Explanation -> Notes -> Quiz)

Run:
  python lc_chains.py
"""

from core.llm_setup import get_llm
from core.tutor_session import TutorSession

def main():
    llm = get_llm()
    session = TutorSession(llm)

    while True:
        print("\n" + "=" * 60)
        print("AI Academic Tutor — Step 7: LangChain Chains")
        print("=" * 60)
        print("1. Run Topic Pipeline (Explanation + Notes + Quiz)")
        print("2. View conversation history")
        print("3. Exit")
        print("=" * 60)

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            topic = input("Enter a topic to generate a full pipeline for: ").strip()

            if topic:
                print("\n[System] Processing sequential chain (this takes a moment)...")
                results = session.run_study_pipeline(topic)

                print("\n=== STEP 1: EXPLANATION ===")
                print(results["explanation"])

                print("\n=== STEP 2: SUMMARY NOTES ===")
                print(results["notes"])

                print("\n=== STEP 3: QUIZ ===")
                print(results["quiz"])

        elif choice == "2":
            session.show_history()

        elif choice == "3":
            print("Goodbye! Keep studying.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()