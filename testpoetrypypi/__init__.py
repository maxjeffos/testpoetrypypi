import poetry_version

from .hello import run

# __version__ = '0.1.0'
__version__ = poetry_version.extract(source_file=__file__)


def main():
    run()
