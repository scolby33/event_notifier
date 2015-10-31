import pytest

from event_notifier.NotifierBackend import ANotifierBackend, PushoverNotifierBackend
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
