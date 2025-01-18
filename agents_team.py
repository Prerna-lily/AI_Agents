from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize tools
duckduckgo_tool = DuckDuckGo()
yfinance_tool = YFinanceTools(
    stock_price=True,
    analyst_recommendations=True,
    stock_fundamentals=True
)

# Define agents
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[duckduckgo_tool],
    instructions=["Always include sources."],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get Financial Data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[yfinance_tool],
    instructions=["Use tables to display data."],
    show_tool_calls=True,
    markdown=True
)

# Define the agent team
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Always include sources.",
        "Use tables to display data.",
        "Summarize comparisons clearly and concisely."
    ],
    show_tool_calls=True,
    markdown=True
)

# Task to compare TSLA and NVDA
task = "Fetch and compare analyst recommendations and stock fundamentals for TSLA and NVDA."

try:
    response = agent_team.run(task)
    print(response)
except Exception as e:
    print("Error occurred while fetching data:", e)

# Independent Testing of YFinanceTools (for debugging)
try:
    print("\nTesting YFinanceTools...")
    tsla_recommendations = yfinance_tool.get_analyst_recommendations("TSLA")
    nvda_recommendations = yfinance_tool.get_analyst_recommendations("NVDA")
    print("TSLA Recommendations:\n", tsla_recommendations)
    print("NVDA Recommendations:\n", nvda_recommendations)
except Exception as e:
    print("Error occurred during independent tool testing:", e)
