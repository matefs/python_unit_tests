import pytest

@pytest.fixture
def important_value():
    important  = True
    return important

@pytest.fixture 
def value_existance():
    value = 1 
    return value 
