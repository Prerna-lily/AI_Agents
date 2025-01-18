from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()

# Initialize the Groq model
try:
    model = Groq(id="llama-3.3-70b-versatile")
    print("Model initialized successfully!")
except Exception as e:
    print(f"Error initializing model: {e}")
    exit()

# Initialize DuckDuckGo tool
try:
    tool = DuckDuckGo()
    print("DuckDuckGo tool initialized successfully!")
except Exception as e:
    print(f"Error initializing DuckDuckGo tool: {e}")
    exit()

# Create an agent
agent = Agent(
    name="ResearchAgent",
    model=model,
    tools=[tool],
    description="An AI agent for researching simulation theory using DuckDuckGo.",
)

# Define the query
query = "Simulation theory"

# Call the agent and handle errors
try:
    print("▰▱▱▱▱▱▱ Thinking...")
    # Fetch response
    response = agent.print_response(query, stream=False)  # Disable streaming to simplify debugging
    print("Response received:")
    print(response)

except Exception as e:
    print(f"Error during agent execution: {e}")
