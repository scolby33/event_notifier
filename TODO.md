#TODO

- [x] Make Sphinx/autodoc work.
- [x] TESTS!
- [x] Sphinx/autodoc and doctest in tox.
- [x] Implement teardown of `mock_pushover_server` fixture (what should its scope be?)
- [x] Use fixtures for test Notifications instead of isntantiating them by hand
- [ ] Properly document the classes using `attrs` for atributes. (`PushoverNotifierBackend`, `Notification`, and `Event` once it's implemented, probably)
- [ ] Flesh out Event class.
- [ ] Implement a storage backend (likely SQLite).
- [ ] Implement Growl backend.
- [ ] Build docs as part of setup.py? Not sure if this is something that is done.
