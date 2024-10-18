from app.commands import Command
from calculator.operations import divide
from calculator.calculation import Calculation
from decimal import Decimal, InvalidOperation

class DivideCommand(Command):
    def __init__(self):
        pass

    def execute(self, *args):
        try: 
            if len(args) != 2:
                raise ValueError("You must provide exactly 2 arguments.")
            a = Decimal(args[0])
            b = Decimal(args[1])

            calculation = Calculation.create(a, b, divide)
            result = calculation.perform()
            print(f"The result of dividing {a} and {b} is {result}")

        except(ValueError, IndexError, InvalidOperation):
            print("Invalid input. Please provide two valid numbers in the format: divide <num1> <num2>")
