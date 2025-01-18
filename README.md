**AI Agents**

The project utilizes AI agents powered by the Groq model and various specialized tools to perform specific tasks, including research and financial analysis. 

The Agent Team is a collaborative system comprising multiple specialized agents working together to tackle complex tasks. It includes:

Web Agent:

Purpose: Performs web-based research using DuckDuckGo.
Instructions: Always include sources in responses.
Features: Markdown support and detailed tool usage logs for transparency.
Finance Agent:

Purpose: Fetches financial data and analyst recommendations using the YFinance tools.
Tools:
Stock price data.
Analyst recommendations.
Stock fundamentals.
Instructions: Displays data using tables for clarity.
Features: Summarizes financial comparisons concisely.
Team Functionality:

The agents collaborate under a unified Agent Team structure, which assigns roles and merges results into a single coherent output.

Libraries and Dependencies:
Install the required dependencies using pip:

bash
```
pip install -r requirements.txt
```

Agent Team
```
python agents_team.py
```

Troubleshooting
Environment Variable Errors:

Ensure .env is correctly set up and accessible.
Dependency Issues:

Verify all required libraries are installed via pip install -r requirements.txt.
Model Initialization Errors:

Confirm that the Groq model ID (llama-3.3-70b-versatile) is valid and supported.
Tool Errors:

Check API limits and ensure DuckDuckGo and YFinance tools are functioning.
