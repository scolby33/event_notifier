import pytest

from event_notifier.NotifierBackend import ANotifierBackend, PushoverNotifierBackend

def test_PushoverNotifierBackend_exists():
    assert isinstance(PushoverNotifierBackend(None, None), PushoverNotifierBackend)
    
def test_PushoverNotifierBackend_is_an_ANotifierBackend():
    assert isinstance(PushoverNotifierBackend(None, None), ANotifierBackend)
