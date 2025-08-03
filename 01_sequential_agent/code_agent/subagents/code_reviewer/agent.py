
from google.adk.agents import LlmAgent
#from google.adk.tools import google_search

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the scorer agent
code_reviewer_agent = LlmAgent(
    name="code_reviewer_agent",
    model=GEMINI_MODEL,
    instruction="""You are an excellent technical writer. 
    write a short paragraph in english about the algorithm used in the below code to be used a code review:
    {python_code} and {test_cases}
    """,
    description="Review python code",
    output_key="comments",
)
