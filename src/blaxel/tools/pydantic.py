from pydantic_ai import RunContext
from pydantic_ai.tools import Tool as PydanticTool
from pydantic_ai.tools import ToolDefinition

from .types import Tool


def get_pydantic_tool(tool: Tool) -> PydanticTool:
    """
    Converts a custom Tool object into a Pydantic AI Tool object.

    Uses the attributes defined in the custom Tool (name, description, input_schema)
    by defining a dynamic 'prepare' function that modifies the ToolDefinition
    generated by Pydantic AI.
    """
    # Select the function to use, prioritizing the async version
    func = tool.coroutine if tool.coroutine else tool.sync_coroutine
    if not func:
        raise ValueError(
            f"Tool '{tool.name}' must have either a coroutine or sync_coroutine defined."
        )

    # Define the prepare function dynamically to capture the 'tool' object
    # Assuming RunContext and ToolDefinition types based on the pydantic_ai example
    async def prepare_tool(
        ctx: RunContext, tool_def: ToolDefinition
    ) -> ToolDefinition | None:
        """Dynamically prepares the ToolDefinition using the custom Tool's attributes."""
        tool_def.name = tool.name  # Override inferred name
        tool_def.description = tool.description  # Override inferred description
        tool_def.parameters_json_schema = tool.input_schema
        return tool_def

    async def pydantic_function(**kwargs):
        return await func(**kwargs)

    # Create the Pydantic AI Tool, passing the function and the prepare hook
    return PydanticTool(
        pydantic_function,
        name=tool.name,
        description=tool.description,
        prepare=prepare_tool,
        takes_ctx=False,
    )


def get_pydantic_tools(tools: list[Tool]) -> list[PydanticTool]:
    return [get_pydantic_tool(tool) for tool in tools]