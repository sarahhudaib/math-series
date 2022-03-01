from math_series import __version__
from math_series.series import *

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_0():
    assert(fibonacci(0) == [])

def test_one():
    actual = fibonacci(1)
    expected = [0]
    assert actual == expected
    
def test_two():
    actual = fibonacci(2)
    expected = [0 , 1]
    assert actual == expected
    
def test_negative():
    assert(fibonacci(-4) == [])
    
def test_fibo_3():
    assert(fibonacci(3) == [0, 1, 1])
    
def test_fibo_7():
    assert (fibonacci(7) == [0, 1, 1, 2, 3, 5, 8])