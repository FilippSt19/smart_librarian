import json
from pathlib import Path
from typing import Any

from app.config import get_settings
from app.engine.tools.base import BaseTool


class BookTools:

    def __init__(self) -> None:
        settings = get_settings()
        self._summaries_path = Path(
            settings.summaries_json_path
        )

    def get_summary_by_title(
        self,
        title: str,
    ) -> str:
        if not self._summaries_path.exists():
            return (
                "I could not find the summaries data file."
            )

        with self._summaries_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            summaries = json.load(file)

        if title in summaries:
            return summaries[title]

        normalized_title = title.strip().casefold()

        for key, value in summaries.items():
            if key.casefold() == normalized_title:
                return value

        return (
            "No summary found for this title. "
            "Please provide the exact title."
        )


class SummaryTool(BaseTool):

    name = "get_summary_by_title"

    description = (
        "Returns the complete summary of a book."
    )

    def __init__(self):

        self.book_tools = BookTools()

    def schema(self) -> dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description":
                                "Exact title of the book."
                        }
                    },
                    "required": [
                        "title"
                    ]
                }
            }
        }

    def execute(
        self,
        **kwargs: Any,
    ) -> str:

        return self.book_tools.get_summary_by_title(
            kwargs["title"]
        )