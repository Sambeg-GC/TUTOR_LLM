# 🎓 Tutor_LLM | AI-Powered Academic Tutor

A console-based AI tutoring system built with **Python** and the **Google Gemini API**, exploring core prompt engineering techniques and LangChain-based application patterns—from a simple LLM call to autonomous agents capable of selecting and using tools.

This project is designed as a **structured lab project**, where each step introduces one new concept while preserving all previous functionality. A single shared `TutorSession` class evolves throughout the project, demonstrating incremental software development and modular design.

---

# ✨ Features

| Status | Feature | File |
|:------:|---------|------|
| ✅ | Session-based conversation with full context history | `llm_integration.py` |
| ✅ | Zero-shot prompting (explain, summarize, simplify) | `zeroshot.py` |
| ✅ | Few-shot prompting (quiz generation, structured notes) | `fewshot.py` |
| ✅ | Chain-of-Thought prompting (step-by-step problem solving) | `chain_of_thought.py` |
| ✅ | Role prompting (Teacher, Examiner, Coach, Subject Expert) | `role_prompting.py` |
| ✅ | Reusable prompt templates with dynamic input substitution | `prompt_templates.py` |
| ✅ | LangChain chains (Topic → Explanation → Notes → Quiz pipeline) | `lc_chains.py` |
| ✅ | Memory system (persist user identity and learning history) | `memory_system.py` |
| ✅ | Agents & tools (calculator, study planner, summarizer) | `lc_agent.py` |
| ✅ | Final integrated console application | `main_app.py` |

---

# 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini API** (`gemini-2.5-flash`)
- **LangChain**
  - `langchain`
  - `langchain-core`
  - `langchain-google-genai`
- **python-dotenv** for environment variable management
- **Retry & Error Handling**
  - `.with_retry()` for transient API failures
  - Custom 45-second backoff mechanism for Gemini rate limits

---

# 📁 Project Structure

```text
Tutor_LLM/
│
├── .env                      # API key             
├── .gitignore
├── requirements.txt          # To be added later
│
├── core/                     # Shared engine
│   ├── __init__.py
│   ├── llm_setup.py          # Gemini client & model configuration
│   └── tutor_session.py      # Shared TutorSession class
│
├── llm_integration.py        # Step 1
├── zeroshot.py               # Step 2
├── fewshot.py                # Step 3
├── chain_of_thought.py       # Step 4
├── role_prompting.py         # Step 5
├── prompt_templates.py       # Step 6
├── lc_chains.py              # Step 7
├── memory_system.py          # Step 8
├── lc_agent.py               # Step 9
└── main_app.py               # Step 10
```

> **Architecture Principle**
>
> The `core/` package contains the reusable engine shared across every step. Each step file is independently executable while importing shared functionality from `core/`, ensuring new features never break previous implementations.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Tutor_LLM.git
cd Tutor_LLM
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure the API Key

Copy the environment template:

```bash
cp .env.example .env
```

Edit the `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

You can obtain a free API key from **Google AI Studio**.

---

## 5. Run the Application

```bash
python main_app.py
```

---

# 📦 Requirements

```text
langchain
langchain-core
langchain-google-genai
python-dotenv
```

Or install directly:

```bash
pip install langchain langchain-core langchain-google-genai python-dotenv
```

---

# 🗺️ Step-by-Step Learning Roadmap

| Step | Topic | Concept Introduced | Status |
|------:|-------|-------------------|:------:|
| 1 | LLM API Integration | Connect to Gemini, maintain session history | ✅ |
| 2 | Zero-Shot Prompting | Instruction-only prompting | ✅ |
| 3 | Few-Shot Prompting | Example-guided output formatting | ✅ |
| 4 | Chain-of-Thought | Step-by-step reasoning | ✅ |
| 5 | Role Prompting | Persona-based prompting | ✅ |
| 6 | Prompt Templates | Reusable LangChain templates | ✅ |
| 7 | LangChain Chains | Sequential multi-step workflows | ✅ |
| 8 | Memory System | Persistent conversation context | ✅ |
| 9 | Agents & Tools | ReAct agent with custom tools | ✅ |
| 10 | Final Integration | Unified production-ready console application | ✅ |

---

# 🔮 Planned Extension — Retrieval-Augmented Generation (RAG)

The current roadmap covers the foundations of prompt engineering and LangChain. A logical next step is implementing a **Retrieval-Augmented Generation (RAG)** pipeline.

Planned enhancements include:

- 📚 ChromaDB or FAISS vector database
- 🧠 Embedding model for semantic search
- 🔍 Similarity search over uploaded study materials
- 📄 Context-grounded responses instead of relying solely on LLM knowledge
- 📊 RAG evaluation using metrics such as:
  - Faithfulness
  - Answer Relevancy
  - Context Precision (RAGAS)

This extension naturally builds upon the concepts introduced in **Chains**, **Memory**, and **Agents**.

---

# 🐛 Known Issues & Fixes

| Issue | Cause | Solution |
|-------|-------|----------|
| **503 UNAVAILABLE** | Temporary Gemini server overload | Automatic retry with exponential backoff |
| **429 RESOURCE_EXHAUSTED** | Free-tier token/rate limit exceeded | Application pauses for 45 seconds before retrying |
| `Response prints as [{'type': 'text', ...}]` | Gemini returns content blocks instead of plain text | `_extract_text()` normalizes all response formats |
| `ModuleNotFoundError: core` | Running scripts from the wrong directory | Execute commands from the project root (`Tutor_LLM/`) |

---

# 📖 Learning Objectives

By completing this project, you will understand:

- Prompt Engineering fundamentals
- Zero-shot & Few-shot prompting
- Chain-of-Thought prompting
- Role-based prompting
- Prompt templating
- LangChain pipelines
- Memory systems
- AI agents and tool calling
- Error handling for production LLM applications
- Incremental software architecture

---

# 👤 Author

**Sambeg G.C.**

---

# 📄 License

This project is intended for **educational and learning purposes**.
```