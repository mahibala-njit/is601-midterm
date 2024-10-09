from calculator.commands import Command  # Ensure this import path is correct

class MenuCommand(Command):
    def execute(self):
        print("Available commands: add, subtract, multiply, divide, menu, exit")
        return ["add", "subtract", "multiply", "divide", "menu", "exit"]  # Return list of commands
