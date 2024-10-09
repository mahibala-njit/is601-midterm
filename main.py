import re
from decimal import Decimal, InvalidOperation
from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.menu import MenuCommand

def main():
    command_handler = CommandHandler()
    
    # Register commands in a loop for better maintainability
    command_classes = {
        "add": AddCommand,
        "subtract": SubtractCommand,
        "multiply": MultiplyCommand,
        "divide": DivideCommand,
        "menu": MenuCommand,
    }

    for command_name, command_class in command_classes.items():
        command_handler.register_command(command_name, command_class)

    print("Welcome to the Calculator REPL!")
    print("Type commands like: add(1, 2), subtract(3, 1), etc.")
    print("Type 'menu' to list available commands.")
    print("Type 'exit' to exit.")

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the calculator.")
            break

        # Use regex to match the command and arguments, allowing for 'menu'
        match = re.match(r"(\w+)(?:\(([^)]*)\))?", user_input)
        
        if match:
            command_name = match.group(1)
            args = match.group(2)  # Get the arguments if present
            
            if args:
                args = args.split(",")  # Split arguments by comma
            else:
                args = []  # No arguments for menu command
            
            try:
                # Convert arguments to Decimal only if there are any
                decimal_args = list(map(Decimal, args)) if args else []
                command_handler.execute_command(command_name, *decimal_args)
            except InvalidOperation:
                print("Invalid input. Please enter valid numbers.")
            except KeyError:
                print(f"No such command: {command_name}. Type 'menu' for available commands.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid command format")


if __name__ == '__main__':
    main()
