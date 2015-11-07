import abc
import os

import sqlalchemy.engine
import sqlalchemy.orm.session
import sqlalchemy.ext.declarative


class AStorageBackend(object,  metaclass=abc.ABCMeta):
    """Abstract class for storage backends. Methods are written for the use of an SQAlchemy database.

    :param storage_location: the location where the database or other storage medium is stored
    """
    @abc.abstractmethod
    def __init__(self, storage_location): # pragma: no cover
        raise NotImplementedError

    def register_notifier_backend_parameters(self, parameters): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def add_event(self, event): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def remove_event(self, event_id): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def _list_events(self): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def add_notification(self, notification): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def remove_notification(self, notification_id): # pragma: no cover
        raise NotImplementedError

    @abc.abstractmethod
    def _list_notifications(self): # pragma: no cover
        raise NotImplementedError

class SQLiteStorageBackend(AStorageBackend):
    """A StorageBackend using the SQLite database engine

    :param storage_location: the path to the file where the SQLite database is stored. If ':memory:', uses an in-memory database
    :type storage_location: str
    """
    def __init__(self, storage_location):
        if storage_location == ':memory:':
            storage_path = storage_location
        else:
            storage_path = os.path.abspath(storage_location)
        self._engine = sqlalchemy.engine.create_engine('sqlite:///{}'.format(storage_path))
        self._Session = sqlalchemy.orm.sessionmaker(bind=self._engine)
        Base.metadata.create_all(self._engine)

    def register_notifier_backend_parameters(self, parameters):
        session = self._Session()
        session.add(parameters)
        session.commit()

    def add_event(self, event):
        pass

    def remove_event(self, event_id):
        pass

    def _list_events(self):
        pass

    def add_notification(self, notification):
        pass

    def remove_notification(self, notification_id):
        pass

    def _list_notifications(self):
        pass

Base = sqlalchemy.ext.declarative.declarative_base()
