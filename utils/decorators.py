import pytest

def regression(func):
    """Marks a test as regression test. """
    return pytest.mark.mandatory(func)
