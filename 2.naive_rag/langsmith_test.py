from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv(override=True, dotenv_path="../.env")



print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY")[:10])
print("LANGCHAIN_PROJECT:", os.getenv("LANGCHAIN_PROJECT"))

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]}
)