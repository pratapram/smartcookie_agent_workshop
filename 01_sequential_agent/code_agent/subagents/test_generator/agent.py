

from google.adk.agents import LlmAgent

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"


test_generator_agent = LlmAgent(
    name="test_generator_agent",
    model=GEMINI_MODEL,
    instruction="""You write test cases for python code.

    You write test cases for python code. {python_code}.
    The test cases should cover all intersting use case.
 
    """,
    description="Write test cases for python functions with details",
    output_key="test_cases",
)
