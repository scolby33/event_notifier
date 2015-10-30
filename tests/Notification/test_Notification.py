import pytest

import datetime

from event_notifier.Notification import Notification

TEST_SUBJECT = 'a'
TEST_MESSAGE = 'b'
TEST_URL = 'http://c.com'
TEST_URL_TITLE = 'c'
TEST_PRIORITY = 1
TEST_TIMESTAMP = datetime.datetime(2015, 1, 1, 12, 31, 4, 14)
TEST_SOUND = 'd'

def test_Notification_requires_subject_and_message():
    with pytest.raises(TypeError):
        Notification()

def test_Notification_accepts_required_arguments():
    testNotification = Notification(TEST_SUBJECT, TEST_MESSAGE)
    assert testNotification.subject == TEST_SUBJECT
    assert testNotification.message == TEST_MESSAGE

def test_Notification_sets_reasonable_defaults_for_optional_arguments():
    testNotification = Notification(TEST_SUBJECT, TEST_MESSAGE)
    assert isinstance(testNotification.url, str)
    assert isinstance(testNotification.url_title, str)
    assert isinstance(testNotification.priority, int)
    assert isinstance(testNotification.timestamp, datetime.datetime)
    assert isinstance(testNotification.sound, str)

def test_Notification_accepts_all_arguments():
    testNotification = Notification(TEST_SUBJECT, TEST_MESSAGE, url=TEST_URL, url_title=TEST_URL_TITLE, priority=TEST_PRIORITY, timestamp=TEST_TIMESTAMP, sound=TEST_SOUND)
    assert testNotification.subject == TEST_SUBJECT
    assert testNotification.message == TEST_MESSAGE
    assert testNotification.url == TEST_URL
    assert testNotification.url_title == TEST_URL_TITLE
    assert testNotification.priority == TEST_PRIORITY
    assert testNotification.timestamp == TEST_TIMESTAMP
    assert testNotification.sound == TEST_SOUND

def test_Notification_rejects_bad_arguments():
    with pytest.raises(TypeError):
        Notification(TEST_SUBJECT, TEST_MESSAGE, timestamp='10')
