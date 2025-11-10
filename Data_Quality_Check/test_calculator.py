from calculator import add, sub, mul, div
import pytest
# import pytest_cov

def test_add():
    assert add(10,5) == 15

def test_sub():
    assert sub(10,5) == 5

def test_mul():
    assert mul(10,5) == 50

def test_div1():
    assert div(10,5) == 2

def test_div2():
    assert div(10,0) == 10

