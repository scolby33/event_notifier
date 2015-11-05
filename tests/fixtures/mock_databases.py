import os

import pytest

@pytest.fixture(scope='session')
def mock_sqlite_storage_path(tmpdir_factory):
    """Obtains a path for a mock SQLite database. Scoped to 'session' so the same file is used for each test."""
    tmp_path = tmpdir_factory.mktemp('db').join('test_db.sqlite').strpath
    storage_path = os.path.abspath(tmp_path)
    return storage_path
    