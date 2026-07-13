# Tutor_LLM

A console-based AI tutor built with Python and the Google Gemini API, demonstrating core prompt engineering techniques and LangChain concepts (chains, memory, agents). Built as a lab project covering prompting fundamentals and LLM integration.

## Features

- Conversational tutoring with persistent context across a session (`core/tutor_session.py`)
- Zero-shot prompting for free-form topic explanations (`zeroshot.py`)
- Few-shot prompting for structured responses (`fewshot.py`)
- Chain-of-Thought (CoT) prompting for step-by-step reasoning problems (`chain_of_thought.py`)
- Centralized LLM client setup with auto-retry on transient errors (`core/llm_setup.py`)
- *(Planned)* Role-based prompting for persona-driven responses
- *(Planned)* Reusable prompt templates
- *(Planned)* LangChain chains for multi-step pipelines
- *(Planned)* Memory system to recall user info and past topics
- *(Planned)* Agents & tools that decide which tool to use

## Tech Stack

- Python
- Google Gemini API — `gemini-2.5-flash` (via `langchain-google-genai`)
- LangChain (`langchain`, `langchain-google-genai`)
- `python-dotenv` for environment variable management
- Built-in retry handling (`.with_retry()`) for transient API errors

## Project Structure

```
Tutor_LLM/
├── .env                    # API keys (not committed)
├── .gitignore
├── requirements.txt        # (to be added)
├── core/
│   ├── __init__.py
│   ├── llm_setup.py         # LLM client setup, retry logic
│   └── tutor_session.py     # Conversational session/context handling
├── llm_integration.py       # Shared LLM call wrapper
├── zeroshot.py               # Zero-shot prompting
├── fewshot.py                 # Few-shot prompting
└── chain_of_thought.py        # Chain-of-Thought prompting
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Tutor_LLM.git
   cd Tutor_LLM
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   Get a free key from [aistudio.google.com](https://aistudio.google.com).

5. Run a script:
   ```bash
   python zeroshot.py
   ```

## Progress

| Step | Topic                      | Status         |
|------|-----------------------------|----------------|
| 1    | LLM API Integration          | ✅ Done         |
| 2    | Zero-Shot Prompting           | ✅ Done         |
| 3    | Few-Shot Prompting             | ✅ Done         |
| 4    | Chain-of-Thought Prompting      | ✅ Done         |
| 5    | Role Prompting                   | 🔲 Not started  |
| 6    | Prompt Templates                  | 🔲 Not started  |
| 7    | LangChain Chains                   | 🔲 Not started  |
| 8    | Memory System                       | 🔲 Not started  |
| 9    | Agents & Tools                       | 🔲 Not started  |
| 10   | Final Integration                     | 🔲 Not started  |

## Notes

- Built with the Google Gemini API (`gemini-2.5-flash`) via LangChain's `langchain-google-genai` integration.
- Includes auto-retry with exponential backoff for transient API errors (e.g. `503 UNAVAILABLE`).

## Author

Sambeg G.C.