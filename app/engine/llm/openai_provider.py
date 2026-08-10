from openai import OpenAI

from app.config import get_settings
from app.engine.llm.base import LLMProvider


class OpenAIProvider(LLMProvider):

    def __init__(self) -> None:
        self.settings = get_settings()

        self.client = OpenAI(
            api_key=self.settings.openai_api_key
        )

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        temperature: float = 0.3,
    ) -> str:

        messages: list[dict[str, str]] = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = self.client.chat.completions.create(
            model=self.settings.chat_model,
            temperature=temperature,
            messages=messages,
        )

        return (
            response.choices[0].message.content
            or ""
        )

    def generate_image(
        self,
        prompt: str,
    ) -> str:

        response = self.client.images.generate(
            model=self.settings.image_model,
            prompt=prompt,
            size="1024x1024",
            quality="low",
        )

        image = response.data[0]

        if image.b64_json:
            return image.b64_json

        raise ValueError(
            "Image generation returned no image data."
        )