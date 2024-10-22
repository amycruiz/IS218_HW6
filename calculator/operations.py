import logging
from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")
    return result

def subtract(a: Decimal, b: Decimal) -> Decimal:
    result = a - b
    logging.info(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a: Decimal, b: Decimal) -> Decimal:
    result = a * b
    logging.info(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"Dividing {a} / {b} = {result}")
    return result
