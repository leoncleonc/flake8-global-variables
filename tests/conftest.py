import os

import pytest


@pytest.fixture(scope='session')
def absolute_path():
    def factory(*files):
        dirname = os.path.dirname(__file__)
        return os.path.join(dirname, *files)

    return factory
