
from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the validator agent
code_generator_agent = LlmAgent(
    name="code_generator_agent",
    model=GEMINI_MODEL,
    instruction="""You are an expert python code generator. 
    Generate a function, and use type hints. Use the most optimal code, and do not write
    comments inside the function.
    
    
    """,
    description="Writes a python function",
    output_key="python_code")
