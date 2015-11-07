import abc
import requests

import sqlalchemy

from event_notifier.exceptions import EventNotifierNotificationDispatchException
from event_notifier.StorageBackend import Base


class ANotifierBackend(object, metaclass=abc.ABCMeta):
    """Abstract class for notifier backends"""
    @abc.abstractmethod
    def dispatch_notification(self, notification): # pragma: no cover
        """Sends a passsed-in notification

        :param notification: a Notification object to be dispatched
        :type notification: event_notifier.Notification.Notification
        :raises EventNotifierNotificationDispatchException: When an error is encountered with dispatching the notification.
        :returns: True if the notification was dispatched correctly
        :rtype: bool
        """
        raise NotImplementedError


class NotifierBackendMeta(type(ANotifierBackend), type(Base)):
    pass


class PushoverNotifierBackend(ANotifierBackend, Base, metaclass=NotifierBackendMeta):
    __tablename__ = 'pushover_notifier_parameters'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    token = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    user = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    device = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return '<PushoverNotifierBackend(token={}, user={}, device={})>'.format(self.token, self.user, self.device)

    def dispatch_notification(self, notification):
        """Sends a passed-in notification

        :param notification: a Notification object to be dispatched
        :type notification: event_notifier.Notification.Notification
        :raises EventNotifierNotificationDispatchException: When an error is encountered with dispatching the notification. Passes the response object from the HTTP POST request to the exception.
        :returns: True if the notification was dispatched correctly
        :rtype: bool
        """
        payload = {
            'token': self.token,
            'user': self.user,
            'title': notification.subject,
            'message': notification.message,
            'device': self.device,
            'url': notification.url,
            'url_title': notification.url_title,
            'priority': notification.priority,
            'timestamp': int(notification.timestamp.timestamp()),
            'sound': notification.sound
        }
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        r = requests.post(
            'https://api.pushover.net:443/1/messages.json',
            data = payload,
            headers = headers
        )
        if r.status_code != 200:
            raise EventNotifierNotificationDispatchException(r)
        return True
