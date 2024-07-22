import pytest

@pytest.mark.slow
def test_slow_function():
    import time
    time.sleep(5)
    assert True

from unittest.mock import MagicMock

@pytest.mark.slow
@pytest.mark.database
def test_database_function():
    db = MagicMock()
    db.is_connected.return_value = True
    assert db.is_connected()

import sys

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on Windows")
def test_not_on_windows():
    assert True


@pytest.mark.skip(reason="not implemented yet")
def test_not_implemented():
    assert True

@pytest.mark.xfail(reason="known bug")
def test_known_bug():
    assert False

@pytest.mark.parametrize("x, y, result", [
    (1, 2, 3),
    pytest.param(1, 1, 3, marks=pytest.mark.xfail),
])
def test_addition(x, y, result):
    assert x + y == result



from unittest.mock import MagicMock

@pytest.mark.database
def test_database_insert():
    db = MagicMock()
    db.query.return_value = [{'id': 1, 'name': 'Alice'}]
    db.insert("INSERT INTO users (name) VALUES ('Alice')")
    result = db.query("SELECT * FROM users WHERE name = 'Alice'")
    assert result is not None

@pytest.mark.database
def test_database_delete():
    db = MagicMock()
    db.query.return_value = None
    db.delete("DELETE FROM users WHERE name = 'Alice'")
    result = db.query("SELECT * FROM users WHERE name = 'Alice'")
    assert result is None

import pytest
from unittest.mock import MagicMock

@pytest.mark.skipif(not MagicMock().is_connected(), reason="database not connected")
def test_database_connection():
    db = MagicMock()
    db.is_connected.return_value = True
    assert db.is_connected()
