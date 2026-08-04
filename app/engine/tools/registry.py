from typing import Any

from app.engine.tools.base import BaseTool


class ToolRegistry:

    def __init__(
        self,
        tools: list[BaseTool],
    ):

        self.tools = {
            tool.name: tool
            for tool in tools
        }

    def schemas(
        self,
    ) -> list[dict[str, Any]]:

        return [
            tool.schema()
            for tool in self.tools.values()
        ]

    def execute(
        self,
        name: str,
        arguments: dict[str, Any],
    ) -> str:

        tool = self.tools.get(name)

        if tool is None:

            raise ValueError(
                f"Unknown tool: {name}"
            )

        return tool.execute(
            **arguments
        )