# app/plugins/add_command.py

from app.commands import Command

class AddCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print(f"The sum is: {result}")
        except ValueError:
            print("Please enter valid numbers.")