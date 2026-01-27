import pytest

@pytest.mark.parametrize("a,b,res", [(1,2,3), (3,4,7), (4,5,9)])
def test_sum(a, b, res):
    print(a+b)
    assert a+b == res
    