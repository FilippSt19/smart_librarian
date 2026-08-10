import re


class ContentFilterService:

    def __init__(
        self,
        blocked_terms: set[str] | None = None,
    ) -> None:
        self.blocked_terms = (
            blocked_terms
            if blocked_terms is not None
            else {
                "idiot",
                "stupid",
                "moron",
                "fuck",
                "fucking",
                "shit",
                "bitch",
                "asshole",
            }
        )

    def contains_inappropriate_language(
        self,
        text: str,
    ) -> bool:

        normalized_text = text.lower()

        return any(
            re.search(
                rf"\b{re.escape(term)}\b",
                normalized_text,
            )
            is not None
            for term in self.blocked_terms
        )