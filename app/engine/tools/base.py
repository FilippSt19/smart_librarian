from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):

    name: str
    description: str

    @abstractmethod
    def schema(self) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute(
        self,
        **kwargs: Any,
    ) -> str:
        pass