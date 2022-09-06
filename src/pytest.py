import pytest

def func(x):
    return  x + 5

def test_method1():
    assert func(3) == 8

    