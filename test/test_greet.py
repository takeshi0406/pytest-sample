import pytest
from src import script


def test_greet():
    assert script.greet("Guido") == "Hello, Guido!"
    assert script.greet("Django") == "Hello, Django!"


@pytest.mark.parametrize(("name", "expected"), [
    ("Jason", "Hello, Jason!"),
    ("Django", "Hello, Django!"),
])
def test_greet_ver2(name, expected):
    assert script.greet(name) == expected
