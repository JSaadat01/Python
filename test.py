import pytest

def f():
    return 100

def test_function():
    assert f() == 100
    if f() == 100:
        print("helloo")

test_function()

