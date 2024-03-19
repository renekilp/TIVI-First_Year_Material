import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For other platforms (Linux, MacOS)
    else:
        _ = os.system('clear')

# Function to clear terminal using ANSI escape codes
def clear_terminal_ansi():
    print("\033[H\033[J")

# Example usage:
print("This is before clearing the terminal.")
# Choose one of the following methods
clear_terminal()
# Or
clear_terminal_ansi()
print("This is after clearing the terminal.")