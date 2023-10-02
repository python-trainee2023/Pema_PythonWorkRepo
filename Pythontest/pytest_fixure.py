import pytest


@pytest.fixture
def func():
    x = 10
    y = 20
    return [x,y]


def test_method1(func):
    assert func[0] == 19


def test_method2(func):
    assert func[0] == 10






