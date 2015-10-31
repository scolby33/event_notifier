import pytest
import responses

from event_notifier.NotifierBackend import ANotifierBackend, PushoverNotifierBackend
from event_notifier.Notification import Notification
from MockPushoverServer import MockPushoverServer
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

class StartMockPushoverServer(MockPushoverServer):
    @responses.activate
    def test_PushoverNotifierBackend_sends_valid_messages():
        testPushoverNotifierBackend = PushoverNotifierBackend(TEST_TOKEN, TEST_USER, TEST_DEVICE)
        testSimpleNotification = Notification(
            subject = TEST_SUBJECT,
            message = TEST_MESSAGE
        )
        testComplexNotification = Notification(
            subject = TEST_SUBJECT,
            message = TEST_MESSAGE,
            url = TEST_URL,
            url_title = TEST_URL_TITLE,
            priority = TEST_PRIORITY,
            timestamp = TEST_TIMESTAMP,
            sound = TEST_SOUND
        )
        testPushoverNotifierBackend.dispatch_notification(testSimpleNotification)
        testPushoverNotifierBackend.dispatch_notification(testComplexNotification)
