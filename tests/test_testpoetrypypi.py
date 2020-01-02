from testpoetrypypi import __version__
import os
import tomlkit

# def test_version():
#     assert __version__ == '0.1.0'

def test_stuff():
    assert 1 == 1

def test_module_version_matches_pyproject_version():
    """Verify that the __version__ in the module is being correctly pulled from the pyproject.toml config"""
    version_from_package_init = __version__

    # this is so that the test finds the pyproject.toml file when run from the command line or from within Pycharm
    this_directory = os.path.dirname(os.path.realpath(__file__))
    pyproject_toml_path = os.path.join(this_directory, "..", "pyproject.toml")

    with open(pyproject_toml_path) as pyproject_file:
        pyproject_contents = pyproject_file.read()

    pyproject_meta_data = tomlkit.parse(pyproject_contents)["tool"]["poetry"]
    version_from_pyproject = pyproject_meta_data["version"]

    assert version_from_package_init == version_from_pyproject
