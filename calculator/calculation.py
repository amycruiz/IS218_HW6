import logging
from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
        logging.info(f"Initialized {self}")
    
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        logging.info(f"Creating a new calculation: {operation.__name__} with {a} and {b}")
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        result = self.operation(self.a, self.b)
        logging.info(f"Performing calculation: {self} = {result}")
        return result

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
