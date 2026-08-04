class SmartLibrarianError(Exception):
    """
    Base application exception.
    """


class ConfigurationError(
    SmartLibrarianError
):
    """
    Raised when configuration is invalid.
    """


class RetrievalError(
    SmartLibrarianError
):
    """
    Raised when semantic retrieval fails.
    """


class EmbeddingError(
    SmartLibrarianError
):
    """
    Raised when embedding generation fails.
    """


class ToolExecutionError(
    SmartLibrarianError
):
    """
    Raised when tool execution fails.
    """


class RepositoryError(
    SmartLibrarianError
):
    """
    Raised when repository access fails.
    """


class LLMProviderError(
    SmartLibrarianError
):
    """
    Raised when the LLM provider fails.
    """