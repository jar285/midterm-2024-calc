'''Subtract plugin for the calculator application'''
# app/plugins/subtract/__init__.py
import logging
from app.commands import Command

class SubstractCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print(f"The result of subtracting {num2} from {num1} is: {result}")
            logging.info(f"Subtraction successful: {num1} - {num2} = {result}")
        except ValueError:
            print("Please enter valid numbers.")
            logging.error("Invalid input for numbers.")
