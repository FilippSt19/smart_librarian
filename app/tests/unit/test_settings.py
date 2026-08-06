from app.config import get_settings


def test_settings_loaded():

    settings = get_settings()

    assert settings.chat_model == "gpt-4.1-mini"
    assert settings.embedding_model == "text-embedding-3-small"
    assert settings.default_n_results > 0