from functools import lru_cache
from pathlib import Path


PROMPTS_DIR = Path(__file__).resolve().parent / "engine" / "prompts"
SYSTEM_PROMPT_PATH = PROMPTS_DIR / "smart_librarian_system.md"


@lru_cache
def get_system_prompt() -> str:
	return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")