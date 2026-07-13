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
        """Displays full conversation history with safety checks for empty lists."""
        print("\n--- Conversation History ---")
        
        # Check if history list has anything inside it
        if not self.history:
            print("[System Notice] The conversation history list is completely empty.")
            return
            
        print(f"[Debug] Printing {len(self.history)} messages from active memory:")
        
        for idx, msg in enumerate(self.history):
            role = msg.__class__.__name__.replace("Message", "")
            # Using repr() as a fallback ensures text prints even if encoding strains the console
            content = msg.content
            print(f"{idx + 1}. [{role}]: {content}\n")
            
        print("-----------------------------\n")

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


# ---- Step 7: LangChain Chains ----
    def run_study_pipeline(self, topic: str) -> dict:
        """Runs a sequential pipeline: Topic -> Explanation -> Summary Notes."""
        from langchain_core.prompts import PromptTemplate
        from langchain_core.output_parsers import StrOutputParser

        # Chain 1: Generate the explanation
        explain_chain = (
            PromptTemplate.from_template("Explain '{topic}' clearly for a beginner student.") 
            | self.llm 
            | StrOutputParser()
        )

        # Chain 2: Take the explanation and extract bullet points
        notes_chain = (
            PromptTemplate.from_template("Based on this explanation, extract 3 key study points:\n\n{explanation}") 
            | self.llm 
            | StrOutputParser()
        )

        # Execute the sequence
        explanation = explain_chain.invoke({"topic": topic})
        notes = notes_chain.invoke({"explanation": explanation})

        # Save the full result to the main session history
        from langchain_core.messages import HumanMessage, AIMessage
        self.history.append(HumanMessage(content=f"Generate pipeline for: {topic}"))
        self.history.append(AIMessage(content=f"Explanation:\n{explanation}\n\nNotes:\n{notes}"))

        return {"explanation": explanation, "notes": notes}
    

# ---- Step 8: Memory System ----
    def save_history(self, filename="tutor_history.json"):
        """Saves current conversation history to a local JSON file."""
        import json
        import os
        
        serialized = []
        for msg in self.history:
            serialized.append({
                "role": msg.__class__.__name__,
                "content": msg.content
            })
            
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(serialized, f, ensure_ascii=False, indent=4)
        
        print(f"\n[Debug] History saved successfully to: {os.path.abspath(filename)}")

    def load_history(self, filename="tutor_history.json"):
        """Loads conversation history from a local JSON file if it exists."""
        import os
        import json
        
        if not os.path.exists(filename):
            print(f"\n[Debug] No saved history file found at: {os.path.abspath(filename)}")
            return
            
        with open(filename, "r", encoding="utf-8") as f:
            serialized = json.load(f)
            
        self.history = []
        for item in serialized:
            role = item.get("role")
            content = item.get("content", "")
            
            if role == "SystemMessage":
                self.history.append(SystemMessage(content=content))
            elif role == "HumanMessage":
                self.history.append(HumanMessage(content=content))
            elif role == "AIMessage":
                self.history.append(AIMessage(content=content))
                
        print(f"\n[Debug] Loaded {len(self.history)} messages from history file.")

    def show_history(self):
        """Displays full conversation history clearly."""
        print("\n--- Conversation History ---")
        if not self.history:
            print("No history found.")
            return
        for msg in self.history:
            role = msg.__class__.__name__.replace("Message", "")
            print(f"[{role}] {msg.content}\n")


# ---- Step 9: Advanced Academic Agent (Math + Summarizer + Planner) ----
    def ask_with_tools(self, user_input: str) -> str:
        """Runs an autonomous academic agent equipped with a calculator tool, 
        plus built-in specialized engines for text summarization and study planning."""
        try:
            from langchain.agents import AgentExecutor, create_react_agent
        except ImportError:
            from langchain_classic.agents import AgentExecutor, create_react_agent
            
        from langchain_core.prompts import PromptTemplate
        from langchain_core.tools import tool

        # 1. Define the native Python calculation tool
        @tool
        def calculate(expression: str) -> str:
            """Useful for executing precise math calculations and formulas. 
            Input must be a raw string mathematical expression like '2 + 2' or '54 * (12 / 3)'."""
            try:
                import math
                allowed_names = {k: v for k, v in vars(math).items() if not k.startswith("__")}
                return str(eval(expression, {"__builtins__": None}, allowed_names))
            except Exception as e:
                return f"Error evaluating expression: {str(e)}"

        tools = [calculate]

        # 2. Design the master academic prompt template with Summarizer and Planner logic
        template = """You are an AI Academic Tutor. You specialize in three main pillars:
1. Precise Mathematics: ALWAYS use the 'calculate' tool for math operations rather than solving them mentally.
2. Text Summarization: When asked to summarize text, format your output with a bold 'TL;DR' paragraph, followed by a bulleted list of 'Key Takeaways', and finish with 3 quick 'Concept Flashcard Questions'.
3. Study Planning: When asked to create a study plan or schedule, always generate a structured Markdown table detailing [Day/Week | Topic to Cover | Estimated Time | Study Strategy].

You have access to the following tools:

{tools}

To use a tool, you MUST use the exact format below:

Thought: Do I need to use a tool? Yes.
Action: the action to take, must be exactly one of [{tool_names}]
Action Input: the mathematical expression to calculate (e.g., "66 + (66 / 77)")
Observation: the result of the tool execution
... (this Thought/Action/Action Input/Observation can repeat if needed)
Thought: Do I need to use a tool? No.
Final Answer: The final response to the student. If you are summarizing or planning, apply the mandatory markdown formatting rules listed above.

If you don't need a tool to answer the question, skip the tool format and just provide the Final Answer directly.

Current Conversation History:
{chat_history}

Student Question: {input}
Thought: {agent_scratchpad}"""

        prompt = PromptTemplate.from_template(template)

        # 3. Format history list into a clean text block
        history_text = ""
        for msg in self.history:
            role = msg.__class__.__name__.replace("Message", "")
            history_text += f"[{role}]: {msg.content}\n"

        # 4. Initialize the ReAct runtime agent sequence
        agent = create_react_agent(self.llm, tools, prompt)
        agent_executor = AgentExecutor(
            agent=agent, 
            tools=tools, 
            verbose=True,
            handle_parsing_errors=True
        )

        # 5. Invoke the execution loop
        response = agent_executor.invoke({
            "input": user_input,
            "chat_history": history_text,
        })
        
        output = response["output"]

        # 6. Append turns and save state
        from langchain_core.messages import HumanMessage, AIMessage
        self.history.append(HumanMessage(content=user_input))
        self.history.append(AIMessage(content=output))
        self.save_history()

        return output