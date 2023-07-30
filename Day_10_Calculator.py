logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def calculator():
    """
    A calculator function that performs basic arithmetic operations.

    This function prompts the user to enter two numbers and an operation symbol. It then performs the requested operation on the two numbers and displays the result. The user can choose to continue calculating with the current result, start a new calculation, or exit the calculator.

    Parameters:
    None

    Returns:
    None
    """
    def get_valid_operator(prompt, valid_choices):
        while True:
            choice = input(prompt)
            if choice in valid_choices:
                return choice
            else:
                for symbol in operations:
                    print(symbol)
                print('Invalid choice! Please try again.')

    def get_valid_input(prompt, valid_choices):
        while True:
            choice = input(prompt).lower()
            if choice in valid_choices:
                return choice
            else:
                print('Invalid choice! Please try again.')

    def get_valid_number(prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Invalid choice! Please try again.')

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "**": lambda x, y: x ** y,
        "%": lambda x, y: x % y,
        "//": lambda x, y: x // y,
        "^": lambda x, y: x ^ y,
    }
    print(logo)

    num1 = None
    should_continue = True

    while should_continue:
        if num1 is None:  # If num1 is None, get a new number
            num1 = get_valid_number("What's the first number?: ")

        for symbol in operations:
            print(symbol)

        operation_symbol = get_valid_operator(
            "Pick an operation: ", [i for i in operations.keys()])

        if operation_symbol.lower() == "exit":
            should_continue = False
            break

        num2 = get_valid_number("What's the next number?: ")

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        choice = get_valid_input(
            "Type 'y' to continue calculating with the current result, 'n' to start a new calculation, or type 'exit' to close the calculator: ", ('y', 'n', 'exit'))
        if choice == "y":
            num1 = result  # Store the result in num1 for future calculations
        elif choice == "n":
            num1 = None  # Reset num1 to None for a new calculation
        elif choice == "exit":
            should_continue = False


calculator()
