from event_notifier.StorageBackend import SQLiteStorageBackend

from tests.fixtures import mock_sqlite_storage_path


def test_sqlite_database_created(mock_sqlite_storage_path):
    testSQLiteStorageBackend = SQLiteStorageBackend(mock_sqlite_storage_path)
    assert False
