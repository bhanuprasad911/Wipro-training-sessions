import pytest

@pytest.fixture
def data():
    return [1,2,3]
def test1(data):
    assert 2 in data
    print(data)
    
def test2(data):
    print(len(data))
    assert len(data)==3