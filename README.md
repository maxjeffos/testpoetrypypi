# testpoetrypypi
A reference-ish implementation of a Python project that uses:
+ Poetry (and pyproject.toml)
+ pytest and Black for testing and linting
+ CircleCI
+ Git Flow (i.e. `master` + `develop` + feature branches)
+ [python-semantic-release](https://pypi.org/project/python-semantic-release/) to compute the next version and publish to PyPI upon merging `develop` into `master`.
