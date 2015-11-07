import attr
import pytest

from event_notifier.Notification import Notification

from tests.constants import *


@pytest.fixture
def mock_simple_notification():
    return Notification(
        subject = TEST_SUBJECT,
        message = TEST_MESSAGE
    )


@pytest.fixture
def mock_complex_notification():
    return Notification(
        subject = TEST_SUBJECT,
        message = TEST_MESSAGE,
        url = TEST_URL,
        url_title = TEST_URL_TITLE,
        priority = TEST_PRIORITY,
        timestamp = TEST_TIMESTAMP,
        sound = TEST_SOUND
    )


@pytest.fixture
def mock_bad_notification():
    @attr.s
    class BadNotification(object):
        subject = attr.ib()

    return BadNotification(TEST_SUBJECT)
