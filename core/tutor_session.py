"""
Shared TutorSession for the AI Academic Tutor project.
This class grows over the course of the project:
  Step 1 -> basic ask() + history
  Step 2 -> zero-shot methods (explain, summarize, simplify)
  Step 4 -> chain-of-thought solving
  Step 5 -> role switching
  ... etc.
Each step file imports this class rather than redefining it.
"""

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


class TutorSession:
    def __init__(self, llm):
        self.llm = llm
        self.history = [
            SystemMessage(content=(
                "You are an AI Academic Tutor. Explain concepts clearly, "
                "patiently, and at a level a student can easily follow. "
                "Keep answers focused and well organized."
            ))
        ]

    # ---- Step 1: core ask/response with session history ----
    def ask(self, user_input: str) -> str:
        self.history.append(HumanMessage(content=user_input))
        response = self.llm.invoke(self.history)
        answer_text = self._extract_text(response.content)
        self.history.append(AIMessage(content=answer_text))
        return answer_text

    @staticmethod
    def _extract_text(content) -> str:
        """
        Normalizes the LLM's response.content, which can be either a plain
        string or a list of content blocks (e.g. [{'type': 'text',
        'text': '...', 'extras': {...}}]) depending on the model version.
        """
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    parts.append(block.get("text", ""))
                elif isinstance(block, str):
                    parts.append(block)
            return "".join(parts)
        return str(content)

    def show_history(self):
        print("\n--- Conversation History ---")
        for msg in self.history:
            role = msg.__class__.__name__.replace("Message", "")
            print(f"[{role}] {msg.content}\n")

    # ---- Step 2: Zero-shot prompting ----
    # No examples are given to the model in any of these — just a direct
    # instruction. The model draws on its own training to produce a
    # well-formed answer.

    def explain(self, topic: str) -> str:
        """Zero-shot explanation of an academic topic."""
        prompt = (
            f"Explain the concept of '{topic}' in simple, clear language "
            f"suitable for a student encountering it for the first time. "
            f"Use a short everyday analogy if it helps, then a brief "
            f"more precise definition."
        )
        return self.ask(prompt)

    def summarize(self, material: str) -> str:
        """Zero-shot summarization of study material into key points."""
        prompt = (
            "Summarize the following study material into concise, "
            "easy-to-review bullet points. Keep only the essential ideas:\n\n"
            f"{material}"
        )
        return self.ask(prompt)

    def simplify(self, concept: str) -> str:
        """Zero-shot simplification of a complex/technical concept."""
        prompt = (
            "Simplify the following concept so a complete beginner can "
            "understand it. Avoid jargon; if a technical term is "
            "unavoidable, define it immediately in plain words:\n\n"
            f"{concept}"
        )
        return self.ask(prompt)

    # ---- Step 3: Few-shot prompting ----
    # Each prompt here includes one worked EXAMPLE of the exact output
    # format before asking for new content on the real topic. This is
    # what makes the structure consistent across runs, unlike zero-shot.

    def generate_quiz(self, topic: str, num_questions: int = 3) -> str:
        """Few-shot MCQ quiz generation with a fixed, repeatable format."""
        prompt = f"""Generate multiple-choice quiz questions in EXACTLY this format.

Example (topic: Cells):
Q1: What is the basic structural and functional unit of all living organisms?
A) Atom
B) Cell
C) Tissue
D) Organ
Answer: B
Difficulty: Easy

---

Now generate {num_questions} new quiz questions, following that exact format,
on this topic: {topic}
"""
        return self.ask(prompt)

    def categorize_notes(self, material: str) -> str:
        """Few-shot structured notes: tags each point by category."""
        prompt = f"""Convert study material into structured notes using EXACTLY this format.

Example (input: "Water boils at 100°C at sea level. This is because at that
temperature, water's vapor pressure equals atmospheric pressure. For example,
at high altitudes water boils at a lower temperature."):

[Key Point] Water boils at 100°C at sea level.
[Definition] Boiling occurs when a liquid's vapor pressure equals the surrounding atmospheric pressure.
[Example] At high altitudes, water boils at a lower temperature due to lower atmospheric pressure.

---

Now convert the following material into the same tagged format
([Key Point], [Definition], [Example], [Formula] — use only tags that apply):

{material}
"""
        return self.ask(prompt)

    # ---- Step 4: Chain-of-Thought prompting ----
    # Instead of asking only for a final answer, we explicitly instruct
    # the model to reason through intermediate steps first. This reduces
    # careless errors on multi-step problems and makes the reasoning
    # itself visible/checkable, not just the result.

    def solve_step_by_step(self, problem: str) -> str:
        """Chain-of-thought solving for academic/reasoning problems."""
        prompt = f"""Solve the following problem. Think through it step by step,
showing your reasoning explicitly before giving the final answer.

Structure your response exactly like this:
Step 1: <first reasoning step>
Step 2: <next reasoning step>
... (as many steps as the problem genuinely needs)
Final Answer: <the final answer, clearly stated on its own line>

Do not skip steps, and do not state the final answer until the
"Final Answer:" line.

Problem: {problem}
"""
        return self.ask(prompt)
    
# ---- Step 5: Role Prompting ----
    def set_role(self, role: str, keep_history: bool = False):
        """Changes the AI's persona. Set keep_history=True to switch mid-chat."""
        personas = {
            "teacher": "You are a patient Socratic Teacher. Guide the student with helpful questions instead of giving direct answers.",
            "examiner": "You are a strict Examiner. Quiz the student on their topic and grade their answers critically.",
            "coach": "You are a motivational Study Coach. Help the student with study habits, time management, and confidence.",
            "expert": "You are an advanced Subject Expert. Provide highly technical, deep-dive academic explanations."
        }
        
        base_prompt = personas.get(role.lower(), (
            "You are an AI Academic Tutor. Explain concepts clearly, "
            "patiently, and at a level a student can easily follow."
        ))
        
        # If keeping history, swap the system prompt at index 0
        if keep_history and len(self.history) > 0 and isinstance(self.history[0], SystemMessage):
            self.history[0] = SystemMessage(content=base_prompt)
        else:
            # Otherwise, reset the history completely
            self.history = [SystemMessage(content=base_prompt)]

# ---- Step 6: Prompt Templates ----
    def generate_study_guide(self, topic: str, focus_area: str) -> str:
        """Generates a structured study guide using a LangChain PromptTemplate."""
        from langchain_core.prompts import PromptTemplate
        
        # Define a reusable template structure with placeholders
        template = PromptTemplate.from_template(
            "Create a comprehensive study guide for the topic: {topic}.\n"
            "Focus heavily on this specific sub-area: {focus_area}.\n"
            "Provide a short summary, 3 core concepts, and 2 review questions."
        )
        
        # Dynamically inject the user variables into the template
        prompt_string = template.format(topic=topic, focus_area=focus_area)
        
        # Send the formatted string through the existing chat history chain
        return self.ask(prompt_string)