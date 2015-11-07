import pytest

from event_notifier.NotifierBackend import ANotifierBackend


def test_ANotifierBackend_cannot_be_instantiated():
    with pytest.raises(TypeError):
        ANotifierBackend()
