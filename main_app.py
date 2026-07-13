import os
import sys
import time

# Ensure local modules can be found correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.llm_setup import get_llm
from core.tutor_session import TutorSession

def print_banner():
    """Prints a clean, polished application layout banner."""
    print("=" * 65)
    print("  🎓 AI ACADEMIC TUTOR — UNIFIED PRODUCTION CONSOLE 🎓  ")
    print("=" * 65)
    print("  ✨ Mode Activated: ReAct Agent Framework")
    print("  🧮 Integrated Tools: Python Calculator Engine")
    print("  📝 Pillars: Precise Math | Summarizer Mode | Study Planner")
    print("=" * 65)
    print("  Type 'exit' or 'quit' to safely save history and close.")
    print("=" * 65 + "\n")

def main():
    # Initialize the tutor session backend matching lc_agent.py setup
    try:
        llm = get_llm()
        session = TutorSession(llm)
        
        # Explicitly reload cross-session history
        session.load_history()
        
        print(f"[System] Connected to LLM engine successfully.")
        print(f"[System] History synchronized ({len(session.history)} messages loaded).\n")
    except Exception as e:
        print(f"[Initialization Error] Failed to spin up tutor engine: {e}")
        sys.exit(1)

    print_banner()

    while True:
        try:
            # Prompt the user for input cleanly
            user_input = input("You: ").strip()
            
            # Check for terminal exit commands
            if user_input.lower() in ['exit', 'quit']:
                print("\n[System] Saving conversation states and synchronizing hard drive...")
                session.save_history()
                print("👋 Goodbye! Happy studying!")
                break
                
            if not user_input:
                continue

            print("\n[Agent Loop Started - Analyzing Intent & Routing Tools]")
            
            # Execute agent reasoning chain
            answer = session.ask_with_tools(user_input)
            
            # Print the structured final tutor answer
            print(f"\nTutor: {answer}\n")
            print("-" * 65)

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n[System] Session interrupted via keyboard. Saving state and closing down safely...")
            session.save_history()
            break
            
        except Exception as e:
            error_str = str(e)
            # Gracefully catch and handle Gemini API Free Tier 429 Quota Throttling
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print("\n" + "!" * 65)
                print("⚠️  [API RATE LIMIT THROTTLE] Free Tier Metric Exhausted.")
                print("   The ReAct reasoning loop used up your local per-minute tokens.")
                print("!" * 65)
                
                # Dynamic visual cooldown wait countdown
                print("⏳ Pausing engine execution loop for 45 seconds to reset quota...")
                for remaining in range(45, 0, -1):
                    sys.stdout.write(f"\r   Resuming loop in {remaining}s... ")
                    sys.stdout.flush()
                    time.sleep(1)
                    
                print("\n\n🔄 Engine reset complete! Please re-type or paste your last question.\n")
                print("-" * 65)
            else:
                # Catch-all for any other unanticipated runtime logic breakdowns
                print(f"\n❌ [Runtime Error Encountered]: {error_str}")
                print("Please verify connection integrity or input string format.\n")
                print("-" * 65)

if __name__ == "__main__":
    main()