"""Agent responsible for web search workflows."""
from __future__ import annotations

import asyncio
from agents import Agent, WebSearchTool, Runner, ModelSettings
from dotenv import load_dotenv

load_dotenv()


search_agent = Agent(
    name="Search Agent",
    instructions="Help the user search the internet and save results if asked.",
    tools=[WebSearchTool()],
    model="gpt-4o-mini-search-preview",
    model_settings=ModelSettings(
        verbosity="low"
    )
)

async def main():
    result = await Runner.run(search_agent, "What was the weather like in New York yesterday?")
    print(result.final_output)

if __name__ == "__main__":

    asyncio.run(main())
    

