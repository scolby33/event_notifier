import abc
import requests

class ANotifierBackend(object, metaclass=abc.ABCMeta):
    """Abstract class for notifier backends"""
    @abc.abstractmethod
    def dispatch_notification(self, notification): # pragma: no cover
        """Sends a passsed-in notification
        
        :param notification: a Notification object to be dispatched
        :type notification: event_notifier.Notification.Notification
        :raises EventNotifierNotificationDispatchException: When an error is encountered with dispatching the notification.
        """
        raise NotImplementedError
            
class PushoverNotifierBackend(ANotifierBackend):
    """A backend to send Pushover notifications"""
    def __init__(self, token, user, device=None):
        """Initializes the PushoverNotifier backend
        
        :param token: The Pushover API token ("APP_TOKEN").
        :param user: The Pushover user/group key to whom the notification will be sent
        :param device: Optional. The user's device name to send the message directly to that device, rather than all of the user's devices (multiple devices may be separated by a comma)
        :type token: str
        :type user: str
        :type device: str
        """
        self.token = token
        self.user = user
        self.device = device
        
    def dispatch_notification(self, notification):
        """Sends a passed-in notification
        
        :param notification: a Notification object to be dispatched
        :type notification: event_notifier.Notification.Notification
        :raises EventNotifierNotificationDispatchException: When an error is encountered with dispatching the notification. Passes the response object from the HTTP POST request to the exception.
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
            'timestamp': notification.timestamp.timestamp(),
            'sound': notification.sound
        }
        headers= {'Content-type': 'application/x-www-form-urlencoded'}
        r = requests.post(
            'https://api.pushover.net:443/1/messages.json',
            data = payload,
            headers = headers
        )
        if r.status_code != 200:
            raise EventNotifierNotificationDispatchException(r)
