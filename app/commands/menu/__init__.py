'''menu command module'''
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        print("Available commands:")
        for command_name in self.command_handler.list_commands():
            print("-", command_name)
