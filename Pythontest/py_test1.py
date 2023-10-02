import pytest


def func(x):
    return x + 5


def test_method1():
    assert func(3) == 8


def test_method2():
    assert func(3) ==9


def test_method3():
    assert  func(3) == 9


def test_method4():
    assert func(3) == 18
