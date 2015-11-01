import pytest
import responses

from event_notifier.exceptions import EventNotifierNotificationDispatchException
from event_notifier.NotifierBackend import ANotifierBackend, PushoverNotifierBackend
from event_notifier.Notification import Notification

from tests.fixtures import mock_pushover_server, mock_bad_pushover_server, mock_simple_notification, mock_complex_notification, mock_bad_notification
from tests.constants import *

def test_PushoverNotifierBackend_exists():
    assert isinstance(PushoverNotifierBackend(TEST_TOKEN, TEST_USER), PushoverNotifierBackend)

def test_PushoverNotifierBackend_is_an_ANotifierBackend():
    assert isinstance(PushoverNotifierBackend(TEST_TOKEN, TEST_USER), ANotifierBackend)

def test_PushoverNotifierBackend_accepts_init_arguments():
    testPushoverNotifierBackend = PushoverNotifierBackend(TEST_TOKEN, TEST_USER, TEST_DEVICE)
    assert testPushoverNotifierBackend.token == TEST_TOKEN
    assert testPushoverNotifierBackend.user == TEST_USER
    assert testPushoverNotifierBackend.device == TEST_DEVICE

@responses.activate
def test_PushoverNotifierBackend_sends_valid_simple_notification(mock_pushover_server, mock_simple_notification):
    testPushoverNotifierBackend = PushoverNotifierBackend(TEST_TOKEN, TEST_USER, TEST_DEVICE)
    assert testPushoverNotifierBackend.dispatch_notification(mock_simple_notification)

@responses.activate
def test_PushoverNotifierBackend_sends_valid_complex_notification(mock_pushover_server, mock_complex_notification):
    testPushoverNotifierBackend = PushoverNotifierBackend(TEST_TOKEN, TEST_USER, TEST_DEVICE)
    assert testPushoverNotifierBackend.dispatch_notification(mock_complex_notification)

@responses.activate
def test_PushoverNotifierBackend_raises_exception_when_a_bad_notification_is_provided(mock_pushover_server, mock_bad_notification):
    testPushoverNotifierBackend = PushoverNotifierBackend(TEST_TOKEN, TEST_USER, TEST_DEVICE)
    with pytest.raises(AttributeError):
        testPushoverNotifierBackend.dispatch_notification(mock_bad_notification)

@responses.activate
def test_PushoverNotifierBackend_raises_exception_when_server_rejects_notification(mock_pushover_server, mock_simple_notification):
    testPushoverNotifierBackend = PushoverNotifierBackend(TEST_TOKEN + 'bad', TEST_USER, TEST_DEVICE)
    with pytest.raises(EventNotifierNotificationDispatchException):
        testPushoverNotifierBackend.dispatch_notification(mock_simple_notification)

@responses.activate
def test_PushoverNotifierBackend_raises_exception_when_server_down(mock_bad_pushover_server, mock_simple_notification):
    testPushoverNotifierBackend = PushoverNotifierBackend(TEST_TOKEN, TEST_USER, TEST_DEVICE)
    with pytest.raises(EventNotifierNotificationDispatchException):
        testPushoverNotifierBackend.dispatch_notification(mock_simple_notification)
