# app/plugins/multiply_command.py

from app.commands import Command

class MultiplyCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"The product of {num1} and {num2} is: {result}")
        except ValueError:
            print("Please enter valid numbers.")