import pytest

from event_notifier.StorageBackend import AStorageBackend


def test_AStorageBackend_cannot_be_instantiated():
    with pytest.raises(TypeError):
        AStorageBackend()
