from app.engine.llm.openai_provider import (
    OpenAIProvider,
)


class ImageGenerationService:

    def __init__(
        self,
        provider: OpenAIProvider | None = None,
    ) -> None:
        self.provider = (
            provider
            if provider is not None
            else OpenAIProvider()
        )

    def generate_book_artwork(
        self,
        title: str,
        author: str,
        genre: str,
        summary: str,
    ) -> str:

        prompt = (
            "Create an original atmospheric book-inspired "
            "illustration based on the following information. "
            "Do not reproduce an existing book cover. "
            "Do not include text, titles, logos, or typography. "
            "Create an original visual interpretation of the "
            "themes, setting, and mood.\n\n"
            f"Book: {title}\n"
            f"Author: {author}\n"
            f"Genre: {genre}\n"
            f"Summary: {summary}"
        )

        return self.provider.generate_image(
            prompt
        )