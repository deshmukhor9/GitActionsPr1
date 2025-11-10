from calculator import add, sub, mul, div
import pytest
# import pytest_cov

def test_add(a,b):
    assert add(10,5) == 15

def test_sub(a,b):
    assert sub(10,5) == 5

def test_mul(a,b):
    assert mul(10,5) == 50

def test_div1(a,b):
    assert div(10,5) == 2

def test_div2(a,b):
    assert div(10,0) == 10

