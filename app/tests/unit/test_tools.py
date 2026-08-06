from app.engine.tools.summary_tool import BookTools


def test_get_summary_by_title():

    tools = BookTools()

    summary = tools.get_summary_by_title(
        "The Hobbit"
    )

    assert summary is not None
    assert len(summary) > 0
    assert isinstance(summary, str)