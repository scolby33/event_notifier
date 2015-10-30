#How to Contribute

##Guidelines
Tests are essential! Do what I say, not what I do, and write tests before code.

Document your code! This project uses `sphinx` and its `autodoc` extension to generate documentation from docstrings. Look at some of the existing code for examples.

##Setting Up the Environment

`event_notifier` is set up in such a way that you don't need many packages installed or crazy virtual environments to get everything working. The following steps can be done with system Python or in a virtualenv.

- Make sure you are using Python 3.5. Other versions will be supported in the future, but Python 3.5 is the sole development version for now.
- Install `tox`: `pip install tox`
- Write your tests and code
- Run `tox`. Fix any failing tests or areas of your contribution that lack test coverage.
- Push your contribution or create a pull request!

`tox` is currently set up to build the docs with `sphinx` to test that they can actually be built. To build them for distribution requires installation of `sphinx` (`pip install sphinx`). This situation remains a work in progress--I would like the ability to create the docs for distribution without needing to add any packages besides `tox`.
