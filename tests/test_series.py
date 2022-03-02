from math_series import __version__
from math_series.series import *

def test_version():
    assert __version__ == '0.1.0'

###################### fibonacci #########################   

def test_fibonacci_0():
    assert(fibonacci(0) == [0])

def test_one():
    actual = fibonacci(1)
    expected = [1]
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
    
###################### LUCAS #########################
    
def test_zero():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_one():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_seven():
    expected = 29
    actual = lucas(7)
    assert actual == expected

def test_eleven():
    expected = 199
    actual = lucas(11)
    assert actual == expected

def test_fifteen():
    expected = 1364
    actual = lucas(15)
    assert actual == expected
    
###################### sum_series #########################    
def test_two():
    expected = 1
    actual = sum_series(2)
    assert actual == expected

def test_three():
    expected = 2
    actual = sum_series(3)
    assert actual == expected

def test_four():
    expected = 3
    actual = sum_series(4)
    assert actual == expected

def test_three_parameters():
    expected = 123
    actual = sum_series(10,2,1)
    assert actual == expected

def test_three_parameterssss():
    expected = 55
    actual = sum_series(10,0,1)
    assert actual == expected