import logging
from app.commands import Command
from calculator.operations import add
from calculator.calculation import Calculation
from decimal import Decimal, InvalidOperation

class AddCommand(Command):
    def __init__(self):
        pass

    def execute(self, *args):
        try: 
            logging.info(f"AddCommand is being executed with arguments: {args}")
            if len(args) != 2:
                raise ValueError("You must provide exactly 2 arguments.")
           
            a = Decimal(args[0])
            b = Decimal(args[1])

            calculation = Calculation.create(a, b, add)
            result = calculation.perform()
            print(f"The result of adding {a} and {b} is {result}")
            logging.info(f"Addition result from AddCommand: {a} + {b} = {result}")

        except(ValueError, IndexError, InvalidOperation) as e:
            logging.error(f"Error during AddCommand execution: {e}")
            print("Invalid input. Please provide two valid numbers in the format: add <num1> <num2>")
