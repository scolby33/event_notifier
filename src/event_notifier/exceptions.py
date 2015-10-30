class EventNotifierException(Exception):
    """Root exception for all event_notifier errors, never raised. Should be used to except all event_notifier errors"""
    pass

class EventNotifierNotificationDispatchException(EventNotifierException):
    """Raised when there is an error dispatching a notification"""
    pass
