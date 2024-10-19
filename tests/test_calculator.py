"Testing calculator"
from calculator import Calculator

def test_addition():
    "Testing addition"
    assert Calculator.add(2,2) == 4

def test_subtraction():
    "Testing subtraction"
    assert Calculator.subtract(2,2) == 0

def test_divide():
    "Testing division"
    assert Calculator.divide(2,2) == 1

def test_multiply():
    "Testing multiplication"
    assert Calculator.multiply(2,2) == 4
