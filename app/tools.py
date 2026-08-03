import json
from pathlib import Path


SUMMARIES_PATH = Path("data/summaries.json")


class BookTools:
    """
    Tools used by the Smart Librarian.
    """

    def __init__(self):

        if not SUMMARIES_PATH.exists():
            raise FileNotFoundError(
                f"{SUMMARIES_PATH} not found."
            )

        with open(
            SUMMARIES_PATH,
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