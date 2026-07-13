# 🎓 Tutor_LLM — AI-Powered Academic Tutor

A console-based AI tutoring system built with Python and the Google Gemini API, exploring core prompt engineering techniques and LangChain-based application patterns — from a simple LLM call all the way up to agents that pick and use tools autonomously.

Built as a structured lab project where each step introduces one new concept, keeping all earlier code intact and growing a single shared `TutorSession` class throughout.

---

## ✨ Features

| Done? | Feature | File |
|-------|---------|------|
| ✅ | Session-based conversation with full context history | `llm_integration.py` |
| ✅ | Zero-shot prompting — explain, summarize, simplify | `zeroshot.py` |
| ✅ | Few-shot prompting — quiz generation, structured notes | `fewshot.py` |
| ✅ | Chain-of-Thought prompting — step-by-step problem solving | `chain_of_thought.py` |
| 🔲 | Role prompting — Teacher, Examiner, Coach, Subject Expert | `role_prompting.py` |
| 🔲 | Reusable prompt templates with dynamic input substitution | `prompt_templates.py` |
| 🔲 | LangChain chains — Topic → Explanation → Notes → Quiz pipeline | `lc_chains.py` |
| 🔲 | Memory system — persist user identity and learning history | `memory_system.py` |
| 🔲 | Agents & tools — calculator, study planner, summarizer | `agents_tools.py` |
| 🔲 | Final integration — single unified console app | `main_app.py` |

---

## 🛠️ Tech Stack
A console-based AI tutoring system built with Python and the Google Gemini API, exploring core prompt engineering techniques and LangChain-based application patterns — from a simple LLM call all the way up to agents that pick and use tools autonomously.

Built as a structured lab project where each step introduces one new concept, keeping all earlier code intact and growing a single shared `TutorSession` class throughout.

---

## ✨ Features

| Done? | Feature | File |
|-------|---------|------|
| ✅ | Session-based conversation with full context history | `llm_integration.py` |
| ✅ | Zero-shot prompting — explain, summarize, simplify | `zeroshot.py` |
| ✅ | Few-shot prompting — quiz generation, structured notes | `fewshot.py` |
| ✅ | Chain-of-Thought prompting — step-by-step problem solving | `chain_of_thought.py` |
| 🔲 | Role prompting — Teacher, Examiner, Coach, Subject Expert | `role_prompting.py` |
| 🔲 | Reusable prompt templates with dynamic input substitution | `prompt_templates.py` |
| 🔲 | LangChain chains — Topic → Explanation → Notes → Quiz pipeline | `lc_chains.py` |
| 🔲 | Memory system — persist user identity and learning history | `memory_system.py` |
| 🔲 | Agents & tools — calculator, study planner, summarizer | `agents_tools.py` |
| 🔲 | Final integration — single unified console app | `main_app.py` |

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini API** — `gemini-2.5-flash` (1,500 free requests/day)
- **LangChain** — `langchain`, `langchain-core`, `langchain-google-genai`
- **python-dotenv** — `.env`-based API key management
- **Built-in retry** — `.with_retry()` with exponential backoff for transient 503/429 errors

---
- **Python 3.10+**
- **Google Gemini API** — `gemini-2.5-flash` (1,500 free requests/day)
- **LangChain** — `langchain`, `langchain-core`, `langchain-google-genai`
- **python-dotenv** — `.env`-based API key management
- **Built-in retry** — `.with_retry()` with exponential backoff for transient 503/429 errors

---

## 📁 Project Structure
## 📁 Project Structure

```
Tutor_LLM/
├── .env                      # API key — never commit this
├── .env.example              # Safe template to share
├── .env                      # API key — never commit this
├── .env.example              # Safe template to share
├── .gitignore
├── requirements.txt          # To be added
│
├── core/                     # Shared engine — imported by every step file
│   ├── __init__.py
│   ├── llm_setup.py          # Gemini client, retry logic, model config
│   └── tutor_session.py      # TutorSession class — grows with each step
│
├── llm_integration.py        # Step 1 — basic ask/response + session history
├── zeroshot.py               # Step 2 — zero-shot prompting
├── fewshot.py                # Step 3 — few-shot prompting
├── chain_of_thought.py       # Step 4 — chain-of-thought prompting
├── role_prompting.py         # Step 5 — role-based personas
├── prompt_templates.py       # Step 6 — reusable LangChain prompt templates
├── lc_chains.py              # Step 7 — LangChain sequential chains
├── memory_system.py          # Step 8 — conversation memory
├── agents_tools.py           # Step 9 — LangChain agent with tools
└── main_app.py               # Step 10 — final integrated console app
```

> **Architecture principle:** `core/` holds the shared engine. Each `stepN_*.py` file at the root is a standalone runnable that imports from `core/` — adding a new step never breaks earlier ones.

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Tutor_LLM.git
cd Tutor_LLM
```
│   ├── llm_setup.py          # Gemini client, retry logic, model config
│   └── tutor_session.py      # TutorSession class — grows with each step
│
├── llm_integration.py        # Step 1 — basic ask/response + session history
├── zeroshot.py               # Step 2 — zero-shot prompting
├── fewshot.py                # Step 3 — few-shot prompting
├── chain_of_thought.py       # Step 4 — chain-of-thought prompting
├── role_prompting.py         # Step 5 — role-based personas
├── prompt_templates.py       # Step 6 — reusable LangChain prompt templates
├── lc_chains.py              # Step 7 — LangChain sequential chains
├── memory_system.py          # Step 8 — conversation memory
├── agents_tools.py           # Step 9 — LangChain agent with tools
└── main_app.py               # Step 10 — final integrated console app
```

> **Architecture principle:** `core/` holds the shared engine. Each `stepN_*.py` file at the root is a standalone runnable that imports from `core/` — adding a new step never breaks earlier ones.

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Tutor_LLM.git
cd Tutor_LLM
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your API key
```bash
cp .env.example .env
# Open .env and set:
# GOOGLE_API_KEY=your_api_key_here
```
Get a free key from [aistudio.google.com](https://aistudio.google.com). The free tier of `gemini-2.5-flash` gives **1,500 requests/day** — plenty for development.

### 5. Run any step
```bash
python zeroshot.py
python fewshot.py
python chain_of_thought.py
# etc.
```

---

## 📦 Requirements

```
langchain
langchain-core
langchain-google-genai
python-dotenv
```

---

## 🗺️ Step-by-Step Progress
### 4. Configure your API key
```bash
cp .env.example .env
# Open .env and set:
# GOOGLE_API_KEY=your_api_key_here
```
Get a free key from [aistudio.google.com](https://aistudio.google.com). The free tier of `gemini-2.5-flash` gives **1,500 requests/day** — plenty for development.

### 5. Run any step
```bash
python zeroshot.py
python fewshot.py
python chain_of_thought.py
# etc.
```

---

## 📦 Requirements

```
langchain
langchain-core
langchain-google-genai
python-dotenv
```

---

## 🗺️ Step-by-Step Progress

| Step | Topic | Concept Introduced | Status |
|------|-------|--------------------|--------|
| 1 | LLM API Integration | Connect to Gemini, session history | ✅ Done |
| 2 | Zero-Shot Prompting | Instruction-only prompts | ✅ Done |
| 3 | Few-Shot Prompting | Example-guided output formatting | ✅ Done |
| 4 | Chain-of-Thought | Explicit step-by-step reasoning | ✅ Done |
| 5 | Role Prompting | Persona switching via system prompt | 🔲 Next |
| 6 | Prompt Templates | Reusable LangChain `PromptTemplate` | 🔲 Planned |
| 7 | LangChain Chains | Sequential multi-step pipelines | 🔲 Planned |
| 8 | Memory System | Cross-turn context & user identity | 🔲 Planned |
| 9 | Agents & Tools | LLM-driven tool selection | 🔲 Planned |
| 10 | Final Integration | Unified console app, all modules | 🔲 Planned |

---

## 🔮 Planned Extension — RAG Pipeline

The 10-step roadmap covers prompt engineering and LangChain fundamentals. A natural next layer beyond Step 10 is a **Retrieval-Augmented Generation (RAG)** system, which would add:

- **Vector database** (ChromaDB or FAISS) to store and index study materials
- **Embedding model** to convert text into semantic vectors
- **Similarity search** to retrieve relevant chunks before each LLM call, grounding answers in uploaded documents rather than model memory alone
- **Evaluation metrics** (faithfulness, answer relevancy, context precision) via frameworks like RAGAS

This keeps RAG as a well-founded extension rather than a separate project — Steps 7–9 (chains, memory, agents) build the LangChain foundation it needs.

---

## 🐛 Known Issues & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `503 UNAVAILABLE` | Transient Gemini server overload | Auto-retried with exponential backoff |
| `429 RESOURCE_EXHAUSTED` | Daily free-tier quota exceeded (20 req/day on newer models) | Use `gemini-2.5-flash` (1,500 req/day) |
| Response prints as `[{'type': 'text', ...}]` | Gemini 3.x returns content blocks, not plain strings | `_extract_text()` in `TutorSession` normalizes both formats |
| `ModuleNotFoundError: core` | Step file run from wrong directory | `cd` into `Tutor_LLM/` before running |

---

## 👤 Author

**Sambeg G.C.**

---

## 📄 License

MIT