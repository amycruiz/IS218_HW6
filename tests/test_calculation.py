"""
Test cases for the Calculation class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("first_operand, second_operand, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('5'), divide, Decimal('2')),
])
def test_calculation_operations(first_operand, second_operand, operation, expected):
    """Testing calculation operations with various inputs"""
    calc = Calculation(first_operand, second_operand, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} with {first_operand} and {second_operand}"

def test_calculation_repr():
    """Testing __repr__ method"""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """Testing division by zero"""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
