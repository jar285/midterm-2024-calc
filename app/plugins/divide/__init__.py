'''Divide plugin for the calculator application'''
# app/plugins/divide/__init__.py
import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self):
        logging.info("Executing DivideCommand")
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                logging.error("Attempted division by zero.")
            else:
                result = num1 / num2
                print(f"The result of dividing {num1} by {num2} is: {result}")
                logging.info(f"DivideCommand execution successful: {num1} / {num2} = {result}")
        except ValueError:
            print("Please enter valid numbers.")
            logging.error("Invalid input for numbers.")
