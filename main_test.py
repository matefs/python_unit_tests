import pytest

@pytest.fixture
def one():
    return 1 


def test_we_are(one):
    assert one == 1

# important_value is from conftext
def test_if_important(important_value):
    assert important_value == True


def test_valor(value):
    assert value

