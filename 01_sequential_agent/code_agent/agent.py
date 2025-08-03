
from google.adk.agents import SequentialAgent

from .subagents.code_generator import code_generator_agent
from .subagents.test_generator import test_generator_agent
from .subagents.code_reviewer import code_reviewer_agent

# Create the sequential agent with minimal callback
root_agent = SequentialAgent(
    name="sa_helper_agent",
    sub_agents=[code_generator_agent,test_generator_agent,code_reviewer_agent],
    description="A pipeline that writes code, comments and also writes test cases",
)


