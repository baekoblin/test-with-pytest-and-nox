# conftest.py

def pytest_collection_modifyitems(items):
    items.reverse()


def pytest_collection_finish(session):
    print(f"Collected {len(session.items)} items")
