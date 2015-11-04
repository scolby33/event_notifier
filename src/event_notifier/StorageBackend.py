import abc
import os

import sqlalchemy.ext.declarative

class AStorageBackend(object,  metaclass=abc.ABCMeta):
    """Abstract class for storage backends
    
    :param storage_location: the location where the database or other storage medium is stored
    """
    @abc.abstractmethod
    def __init__(self, storage_location): # pragma: no cover
        raise NotImplementedError
        
    @abc.abstractmethod
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

Base = sqlalchemy.ext.declarative.declarative_base()
