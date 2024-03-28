# app/plugins/subtract_command.py

from app.commands import Command

class SubtractCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print(f"The result of subtracting {num2} from {num1} is: {result}")
        except ValueError:
            print("Please enter valid numbers.")