"""
Shared LLM setup for the AI Academic Tutor project.
Every step (2, 3, 4, ...) imports get_llm() from here instead of
re-writing the connection logic — one place to change models/providers.
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Loads variables from a .env file in the project root (if present) into
# the environment. Safe to call even if no .env file exists — it just
# does nothing in that case, so this won't break setups that export the
# key manually instead.
load_dotenv()


def get_llm(temperature: float = 0.5, max_tokens: int = 2048):
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY (or GEMINI_API_KEY) not found.\n"
            "Either create a .env file in the project root with:\n"
            "  GOOGLE_API_KEY=your-key-here\n"
            "or export it directly in your shell:\n"
            "  export GOOGLE_API_KEY='your-key-here'"
        )
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=temperature,
        max_output_tokens=max_tokens,
    )
    # Auto-retry on transient errors (like 503 UNAVAILABLE) with
    # exponential backoff: waits a bit longer between each retry,
    # up to 4 attempts total, before finally raising the error.
    return llm.with_retry(
        stop_after_attempt=4,
        wait_exponential_jitter=True,
    )