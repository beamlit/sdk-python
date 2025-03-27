import asyncio

from dotenv import load_dotenv

load_dotenv()

from logging import getLogger

from llama_index.core.agent.workflow import (AgentStream, ReActAgent,
                                             ToolCallResult)
from llama_index.core.workflow import Context

from blaxel.models import bl_model
from blaxel.tools import BlTools

logger = getLogger(__name__)


MODEL = "gpt-4o-mini"
# MODEL = "xai-grok-beta"
# MODEL = "deepseek-chat"
# MODEL = "mistral-large-latest"
# MODEL = "claude-3-5-sonnet"
# MODEL = "cohere-command-r-plus" # x -> Error in step 'run_agent_step': 'async for' requires an object with __aiter__ method, got generator
# MODEL = "gemini-2-0-flash" # x -> Error in step 'run_agent_step': Expecting property name enclosed in double quotes

async def main():
    async with BlTools(["blaxel-search"]) as bl_tools:
        tools = bl_tools.to_llamaindex()
        model = await bl_model(MODEL).to_llamaindex()

        agent = ReActAgent(llm=model, tools=tools, system_prompt="You are a helpful assistant. Maximum number of tool call is 1.")
        context = Context(agent)

        input = "What is the current weather in San Francisco ?"
        # input = "Hello world"
        handler = agent.run(input, ctx=context)
        async for ev in handler.stream_events():
            if isinstance(ev, ToolCallResult):
                logger.info(f"Call {ev.tool_name} with {ev.tool_kwargs}\nReturned: {ev.tool_output}")
        response = await handler
        logger.info(response)

if __name__ == "__main__":
    asyncio.run(main())