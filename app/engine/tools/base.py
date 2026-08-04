from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Unique tool name exposed to callers."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable tool description."""

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """Execute the tool using keyword arguments."""
