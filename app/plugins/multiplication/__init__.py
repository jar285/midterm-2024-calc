'''multiplication plugin'''
# app/plugins/multiplication/__init__.py
import logging
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self):
        logging.info("Executing MultiplyCommand")
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"The result of multiplying {num1} by {num2} is: {result}")
            logging.info(f"MultiplyCommand execution successful: {num1} * {num2} = {result}")
        except ValueError:
            print("Please enter valid numbers.")
            logging.error("Invalid input for numbers.")
