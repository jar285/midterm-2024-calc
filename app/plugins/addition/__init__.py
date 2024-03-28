'''Addition plugin for calculator application'''
import logging
from app.commands import Command

class AddCommand(Command):
    def execute(self):
        logging.info("Executing AddCommand")
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            logging.info(f"AddCommand execution successful: {num1} + {num2} = {result}")
            print(f"The sum is: {result}")
        except ValueError:
            logging.error("Error in AddCommand: Invalid input for numbers.")
            print("Please enter valid numbers.")
