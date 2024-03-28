# app/plugins/divide_command.py

from app.commands import Command

class DivideCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result of dividing {num1} by {num2} is: {result}")
        except ValueError:
            print("Please enter valid numbers.")