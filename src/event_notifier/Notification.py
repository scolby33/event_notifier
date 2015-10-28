import attr
import datetime

def is_datetime(instance, attribue, value):
    if not isinstance(value, datetime.datetime):
         raise ValueError('timestamp must be a datetime.datetime object')

@attr.s
class Notification(object):
    """An object representing a notification ready to be sent. Generally will be passed to a NotifierBackend for dispatching."""
    subject = attr.ib()
    message = attr.ib()
    url = attr.ib(default=str())
    url_title = attr.ib(default=str())
    priority = attr.ib(default=0)
    timestamp = attr.ib(default=datetime.datetime.now(), validator=is_datetime)
    sound = attr.ib(default=str())
