from app.commands import Command
from calculator.operations import multiply
from calculator.calculation import Calculation
from decimal import Decimal, InvalidOperation

class MultiplyCommand(Command):
    def __init__(self):
        pass

    def execute(self, *args):
        try: 
            if len(args) != 2:
                raise ValueError("You must provide exactly 2 arguments.")
            a = Decimal(args[0])
            b = Decimal(args[1])

            calculation = Calculation.create(a, b, multiply)
            result = calculation.perform()
            print(f"The result of multiplying {a} and {b} is {result}")

        except(ValueError, IndexError, InvalidOperation):
            print("Invalid input. Please provide two valid numbers in the format: multiply <num1> <num2>")
