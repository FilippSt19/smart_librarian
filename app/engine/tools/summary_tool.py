import json
from pathlib import Path

from app.config import get_settings


class BookTools:
    """
    Tools used by the Smart Librarian.
    """

    def __init__(self):
        self.settings = get_settings()
        self.summaries_path = Path(
            self.settings.summaries_json_path
        )

        if not self.summaries_path.exists():
            raise FileNotFoundError(
                f"{self.summaries_path} not found."
            )

        with open(
            self.summaries_path,
            "r",
            encoding="utf-8"
        ) as file:
            self.book_summaries = json.load(file)

    def get_summary_by_title(
        self,
        title: str,
    ) -> str:
        """
        Return the full summary for an exact title.
        """

        return self.book_summaries.get(
            title,
            "Summary not found."
        )
