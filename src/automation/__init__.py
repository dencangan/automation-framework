import os

_ROOT = os.path.abspath(os.path.dirname(__file__))


def point_to_file(file):
    return os.path.join(_ROOT, file)