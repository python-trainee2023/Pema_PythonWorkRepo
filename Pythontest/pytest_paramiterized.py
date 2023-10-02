import pytest


@pytest.mark.parametrize("a, b, c" [(10, 20, 200), (20,40,500)])
def test_method(a, b, c):
    assert a*b == c

