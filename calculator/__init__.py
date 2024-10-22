import logging
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        logging.info(f"Performing operation with {a} and {b}")
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        result = calculation.perform()
        logging.info(f"Result of operation: {result}")
        return result
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        logging.info(f"Adding {a} + {b}")
        return Calculator._perform_operation(a, b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        logging.info(f"Subtracting {a} - {b}")
        return Calculator._perform_operation(a, b, subtract)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        logging.info(f"Multiplying {a} * {b}")
        return Calculator._perform_operation(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        logging.info(f"Dividing {a} / {b}")
        return Calculator._perform_operation(a, b, divide)
