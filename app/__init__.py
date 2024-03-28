'''App module for the main application'''
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Check if it's a subclass of Command
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        # Dynamically load all command plugins
        self.load_plugins()

        # Explicitly register MenuCommand with command_handler
        menu_command = MenuCommand(self.command_handler)
        self.command_handler.register_command("menu", menu_command)

        print("Type 'exit' to exit.")
        while True:
            command_input = input(">>> ").strip()
            self.command_handler.execute_command(command_input)
