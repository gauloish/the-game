import sys

from time import sleep
from os.path import join
from pathlib import Path


def resolve(path: str) -> str:
    """Get and resolve path

    Args:
        path (str): image path

    Returns:
        path (str): path resolved
    """

    if sys.platform in ["win32", "cygwin", "msys"]:
        path.replace("/", "\\")

    return join(Path.cwd(), path)


def wait(milliseconds: int) -> None:
    """Wait milliseconds

    Args:
        milliseconds: int
    """
    sleep(float(milliseconds) / 1000)
