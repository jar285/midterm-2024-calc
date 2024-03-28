'''This file contains the tests for the commands in the app/commands directory.'''
import pytest
from app import App
from app.plugins.greet import GreetCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.addition import AddCommand
from app.plugins.substract import SubtractCommand
from app.plugins.multiplication import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_greet_command(capfd):
    """Test that the GreetCommand outputs 'Hello, World!'."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Using underscore to ignore the 'err' variable.
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    """Test that the GoodbyeCommand outputs 'Goodbye'."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()  # Using underscore to ignore the 'err' variable since it's not used.
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_add_command(capfd, monkeypatch):
    """Test that the AddCommand correctly adds two numbers."""
    # Simulate user entering '5' and '3' as inputs
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = AddCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The sum is: 8.0" in out, "The AddCommand should correctly add two numbers"

def test_subtract_command(capfd, monkeypatch):
    """Test that the SubtractCommand correctly subtracts two numbers."""
    # Simulate user entering '10' and '3' as inputs
    inputs = iter(['10', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = SubtractCommand()
    command.execute()
    out, _ = capfd.readouterr()
    # Adjust the expected output string to match the actual format
    assert "The result of subtracting 3.0 from 10.0 is: 7.0" in out, "The SubtractCommand should correctly subtract two numbers"

def test_multiply_command(capfd, monkeypatch):
    """Test that the MultiplyCommand correctly multiplies two numbers."""
    # Simulate user entering '6' and '7' as inputs
    inputs = iter(['6', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = MultiplyCommand()
    command.execute()
    out, _ = capfd.readouterr()
    # Adjust the expected output string to exactly match the actual format
    assert "The product of 6.0 and 7.0 is: 42.0" in out, "The MultiplyCommand should correctly multiply two numbers"

def test_divide_command(capfd, monkeypatch):
    """Test that the DivideCommand correctly divides two numbers."""
    # Simulate user entering '10' and '2' as inputs for the first test
    inputs = iter(['10', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "The result of dividing 10.0 by 2.0 is: 5.0" in out, "The DivideCommand should correctly divide two numbers"

    # Test division by zero scenario by simulating '10' and '0' as inputs
    inputs = iter(['10', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    command.execute()
    out, _ = capfd.readouterr()
    assert "Error: Cannot divide by zero." in out, "The DivideCommand should handle division by zero properly"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
