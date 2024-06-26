# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview

This midterm requires the development of an advanced Python-based calculator application. Designed to underscore the importance of professional software development practices, the application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.
## Video demonstration - [here](https://www.loom.com/share/f85e026e792f48e9964ba1fc11b6bad9?sid=7c28a873-d0ca-4d83-a3a8-76870b6530a2)

## Pytest --pylint --cov video - [here](https://www.loom.com/share/9447981ac1a247e9a4c369230f6c79b2?sid=c837728a-d579-4f6e-a0df-4c06866d3928)

## Project Submission

# Setup

## Setup Instructions
1. Clone the repo
2. CD into the project folder
3. Create a virtual environment
4. Activate the virtual environment (VE)
5. Install Requirements

## Test Commands
- `pytest` run all tests
- `pytest --pylint --cov` <- Run Pylint and Coverage (Can be run independently)

# Usage

## Functionlity

### Calculator Operations:

Basic arithmetic operations like add, subtract, multiply, and divide can be performed. With the help of the plugin architecture and dynamic loading design, we can add new features dynamically in the plugins folder without any hardcoding.

commands for the specific operation:

- `addition` - Addition
- `substract` - Subtraction
- `multiplication` - Multiplication
- `divide` - Division
- `menu` - Shows the list of commands
- `exit` - Exit the application
  
Dont worry about greet, exit and goodbye, those are just templates, feel free to modify them as you like.

menu command is to show all the available commands and will append the list if any new plugin is added in the future. The plugin names are parsed directly to show the list.

### History Management:

Effective data management methods are employed to handle the data.

commands to handle the data:

- `load` - Loads the history of operations performed
- `clear` - Clears the history
- `delete` - Deletes only specified index data 
- `save` - Saves your history of operations performed

./data/calculation_history.csv contains the history of operations. The system effectively reads and writes the CSV file.

### Configuration via Environment Variables:

The application configuration details, development, and testing environment variables are stored in .env file.

https://github.com/jar285/midterm-2024-calc/blob/ff04f17f202744a0e3050b47f84445e9e9122c99/app/__init__.py#L30-L37

### REPL Interface:

This application works on the Read-Evaluate-Print-Loop pattern.

<img width="724" alt="Captura de pantalla 2024-03-29 a la(s) 10 51 20 p m" src="https://github.com/jar285/midterm-2024-calc/assets/114256420/393f3550-6faf-4021-8b1b-2055496cd684">

## Design Patterns

### Implementation and Application:

This application used and implemented various design patterns. *Facade pattern* was used for the Pandas data manipulation. The *Command pattern* is the REPL structure the application has and the application's code structure is flexible and scalable using *Factory Method*, *Singleton*, and *Strategy Patterns*.

The provided implementation demonstrates the use of several design patterns:

1. **Singleton Pattern**:
   The `App` class serves as a singleton by ensuring that only one instance of the class can exist within the application. This is achieved by having a private constructor and a static method (`__init__`) that controls the instantiation of the class.

   https://github.com/jar285/midterm-2024-calc/blob/ff04f17f202744a0e3050b47f84445e9e9122c99/app/__init__.py#L11-L18

2. **Factory Method Pattern**:
   The `CommandHandler` class acts as a factory for creating command objects (`Command` instances). It provides a method `register_command` to register different types of commands and another method `execute_command` to execute these commands based on their names.

   https://github.com/jar285/midterm-2024-calc/blob/ff04f17f202744a0e3050b47f84445e9e9122c99/app/commands/__init__.py#L10-L32

3. **Command Pattern**:
   The `Command` abstract base class defines an interface for executing commands (`execute` method). Concrete command classes (for example `AddCommand`) implement this interface, encapsulating specific operations. This pattern decouples the sender (invoker of commands) from the receiver (objects performing the actions), allowing for extensibility and flexibility.

   https://github.com/jar285/midterm-2024-calc/blob/ff04f17f202744a0e3050b47f84445e9e9122c99/app/plugins/addition/__init__.py#L8-L10

4. **Iterator Pattern**:
   The `load_plugins` method in the `App` class iterates over all modules in the `app.plugins` package using `pkgutil.iter_modules`. It dynamically loads and initializes plugin classes, demonstrating the use of the iterator pattern to traverse through a collection of items (modules) without exposing the underlying representation.

   https://github.com/jar285/midterm-2024-calc/blob/ff04f17f202744a0e3050b47f84445e9e9122c99/app/__init__.py#L40-L53

5. **Template Method Pattern**: The `Command` class defines an abstract method `execute()`, which concrete command classes must implement. This enforces a template for executing commands, allowing for customization of specific operations while maintaining a consistent interface across different commands.

6. **Strategy Pattern** (implied): While not explicitly implemented as a separate class, the `execute()` method in each concrete command class represents a strategy for performing specific operations. By encapsulating these strategies within command objects, the application can dynamically select and execute different strategies at runtime.

### Try/Catch/Except
Implemented exceptions to illustrate "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP)

   https://github.com/jar285/midterm-2024-calc/blob/ff04f17f202744a0e3050b47f84445e9e9122c99/app/plugins/multiplication/__init__.py#L8-L37

  ## Testing and Code Quality

### Comprehensive tests using pytest:

The test cases are in the folder tests. Majorly used unit testing and assertions to check all possible outcomes. These test cases helped to increase the application's robustness.

- `pytest` run all tests
- `pytest --pylint --cov` <- Run Pylint and Coverage (Can be run independently)

test coverage = 96%

<img width="732" alt="Captura de pantalla 2024-03-29 a la(s) 11 04 32 p m" src="https://github.com/jar285/midterm-2024-calc/assets/114256420/56894d31-92ac-49e7-913c-ff9c10754713">

(There is a warning, will be fix soon, however everything works )

## Version Control, Documentation, and Logging

GitHub Actions performs all the tests while pushing or merging the code.

### Commit History:

This repo has kept a sequential and informative commit history for any reference

### Logging Practices:

Dynamic logging configuration through environment variables is performed. A professional logging system is designed and logs will contain all the critical steps while performing any operation. Detailed application operations, data manipulations, errors, and informational messages are provided using Logging. This system also retrieves and displays errors and handles exceptions without crashing the applications. Logging is majorly used in this application rather than print statements.

- `logging.info`- logs what happened in the line of code
- `logging.error` - logs the error that occurred after the line of code

https://github.com/jar285/midterm-2024-calc/blob/ff04f17f202744a0e3050b47f84445e9e9122c99/app/plugins/multiplication/__init__.py#L8-L19

<img width="590" alt="Captura de pantalla 2024-03-29 a la(s) 11 08 19 p m" src="https://github.com/jar285/midterm-2024-calc/assets/114256420/5624d24e-f512-4104-85ea-2deb0887684b">







