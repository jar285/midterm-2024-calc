'''Commands package'''
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        # Easier to ask for forgiveness than permission (EAFP) - Use when it's going to most likely work
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

    def list_commands(self):
        """Return a list of registered command names."""
        return list(self.commands.keys())
