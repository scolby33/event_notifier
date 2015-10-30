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

These instructions currently don't work for building the docs. For that, you will need to install `sphinx` as well. This functionality will be implemented with `tox` in the future.
