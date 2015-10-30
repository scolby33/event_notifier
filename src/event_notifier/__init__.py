from .exceptions import EventNotifierException, EventNotifierNotificationDispatchException

from . import Event
from . import Notification

from .StorageBackend import AStorageBackend
from .NotifierBackend import ANotifierBackend, PushoverNotifierBackend


__version__ = '0.0.1'

__title__ = 'event_notifier'
__description__ = 'A Python3 package for unified processing and dispatching of various notifications.'
__url__ = 'https://github.com/scolby33/event_notifier'

__author__ = 'Scott Colby'
__email__ = ''

__license__ = 'Other/Proprietary License'
__copyright__ = 'Copyright (c) 2015 Scott Colby'


__all__ = [
    'Event',
    'Notification',
    'AStorageBackend',
    'ANotifierBackend',
    'PushoverNotifierBackend'
]
