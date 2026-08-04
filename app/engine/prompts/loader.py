from pathlib import Path


class PromptLoader:

    @staticmethod
    def load(
        path: Path,
    ) -> str:

        if not path.exists():

            raise FileNotFoundError(
                f"Prompt not found: {path}"
            )

        return path.read_text(
            encoding="utf-8"
        ).strip()
