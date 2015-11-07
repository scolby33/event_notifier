import os

import pytest

import sqlalchemy.engine
import sqlalchemy.ext.declarative
import sqlalchemy.orm.session
import sqlalchemy.schema

from event_notifier.StorageBackend import Base, SQLiteStorageBackend


@pytest.fixture(scope='session')
def mock_sqlite_storage_path(tmpdir_factory):
    """Obtains a path for a mock SQLite database. Scoped to 'session' so the same file is used for each test."""
    tmp_path = tmpdir_factory.mktemp('db').join('test_db.sqlite').strpath
    storage_path = os.path.abspath(tmp_path)
    return storage_path


@pytest.fixture(scope='session')
def mock_sqlite_setup(request, mock_sqlite_storage_path):
    testSQLiteStorageBackend = SQLiteStorageBackend(mock_sqlite_storage_path)
    metadata = sqlalchemy.schema.MetaData(testSQLiteStorageBackend._engine)
    metadata.reflect()
    for table in metadata.tables.values():
        for fk in table.foreign_keys:
            testSQLiteStorageBackend._engine.execute(sqlalchemy.schema.DropConstraint(fk.constraint))
    metadata.drop_all()

    Base.metadata.create_all()
