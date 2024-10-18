from app.commands import Command
from calculator.operations import add
from calculator.calculation import Calculation
from decimal import Decimal, InvalidOperation

class AddCommand(Command):
    def __init__(self):
        pass

    def execute(self, *args):
        try: 
            if len(args) != 2:
                raise ValueError("You must provide exactly 2 arguments.")
            a = Decimal(args[0])
            b = Decimal(args[1])

            calculation = Calculation.create(a, b, add)
            result = calculation.perform()
            print(f"The result of adding {a} and {b} is {result}")

        except(ValueError, IndexError, InvalidOperation):
            print("Invalid input. Please provide two valid numbers in the format: add <num1> <num2>")
