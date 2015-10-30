import pytest

from event_notifier.NotifierBackend import ANotifierBackend, PushoverNotifierBackend

TEST_TOKEN = 'a'
TEST_USER = 'b'
TEST_DEVICE = 'c'

def test_PushoverNotifierBackend_exists():
    assert isinstance(PushoverNotifierBackend(TEST_TOKEN, TEST_USER), PushoverNotifierBackend)
    
def test_PushoverNotifierBackend_is_an_ANotifierBackend():
    assert isinstance(PushoverNotifierBackend(TEST_TOKEN, TEST_USER), ANotifierBackend)
