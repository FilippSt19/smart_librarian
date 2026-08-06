from app.repositories import ChromaBookRepository


def test_repository_created():

    repository = ChromaBookRepository()

    assert repository is not None