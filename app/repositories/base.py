from abc import ABC, abstractmethod
from typing import Any


class BookRepository(ABC):

    @abstractmethod
    def add_document(
        self,
        document_id: str,
        document: str,
        embedding: list[float],
        metadata: dict[str, Any],
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        embedding: list[float],
        n_results: int,
        where: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def count_documents(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def delete_document(
        self,
        document_id: str,
    ) -> None:
        raise NotImplementedError