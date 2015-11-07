import attr
import datetime


@attr.s
class Notification(object):
    """An object representing a notification ready to be sent. Generally will be passed to a NotifierBackend for dispatching."""
    subject = attr.ib()
    message = attr.ib()
    url = attr.ib(default=str())
    url_title = attr.ib(default=str())
    priority = attr.ib(default=0)
    timestamp = attr.ib(default=datetime.datetime.now(), validator=attr.validators.instance_of(datetime.datetime))
    sound = attr.ib(default=str())
