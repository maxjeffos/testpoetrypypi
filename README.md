# testpoetrypypi
A reference-ish implementation of a Python project that uses Poetry (and pyproject.toml), CircleCI, Git Flow (i.e. `master` + `develop` + feature branches) and semantic-release to compute the next version and publish to PyPI upon merging `develop` into `master`.


## Some useful Poetry commands for me to remember:
`poetry install`

`poetry run pytest`

`poetry run testpoetrypypi`

`poetry run semantic-release version --noop`
