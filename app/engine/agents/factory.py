from app.engine.agents.smart_librarian import (
    SmartLibrarianAgent,
)


class AgentFactory:

    @staticmethod
    def create(
        name: str = "smart_librarian",
    ):

        if name == "smart_librarian":

            return SmartLibrarianAgent()

        raise ValueError(
            f"Unknown agent: {name}"
        )