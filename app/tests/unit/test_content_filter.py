from app.services.content_filter_service import (
    ContentFilterService,
)


def test_detects_inappropriate_language() -> None:
    content_filter = ContentFilterService()

    assert content_filter.contains_inappropriate_language(
        "You are an idiot."
    )


def test_allows_appropriate_language() -> None:
    content_filter = ContentFilterService()

    assert not content_filter.contains_inappropriate_language(
        "Recommend me a fantasy book about friendship."
    )


def test_does_not_match_partial_words() -> None:
    content_filter = ContentFilterService()

    assert not content_filter.contains_inappropriate_language(
        "I enjoy classical literature."
    )


def test_filter_is_case_insensitive() -> None:
    content_filter = ContentFilterService()

    assert content_filter.contains_inappropriate_language(
        "You are an IDIOT."
    )