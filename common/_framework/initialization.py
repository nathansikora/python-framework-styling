from os import environ, getcwd
from pathlib import Path

from .constants import Values, Environment


def _get_base_path() -> str:
    cur_path = Path(getcwd())
    while cur_path.name != Values.BASE_FOLDER_NAME:
        cur_path = cur_path.parent
    return str(cur_path)


if Environment.BASE_PATH not in environ:
    environ[Environment.BASE_PATH] = _get_base_path()
