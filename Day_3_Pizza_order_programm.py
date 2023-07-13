# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.


def pizza_order_programm():
    def get_valid_input(prompt, valid_choices):
        while True:
            choice = input(prompt).lower()
            if choice in valid_choices:
                return choice
            else:
                print('Invalid choice! Please try again.')

    print("Welcome to Python Pizza Deliveries!")
    size = get_valid_input(
        "What size pizza do you want? S, M, or L ", ['s', 'm', 'l'])
    add_pepperoni = get_valid_input(
        "Do you want pepperoni? Y or N ", ['y', 'n'])
    more_cheese = get_valid_input(
        "Do you want extra cheese? Y or N ", ['y', 'n'])

    price = 0
    if more_cheese == 'y':
        price += 1
    sizes = {'s': 15, 'm': 20, 'l': 25}
    peppperoni = {'s': 2, 'm': 3, 'l': 3}
    price += sizes.get(size, 0)
    price += peppperoni.get(size, 0) if add_pepperoni == 'y' else 0
    if size not in sizes:
        return 'Invalid pizza size!'
    if add_pepperoni not in ['y', 'n']:
        return 'Invalid choice for pepperoni!'
    if more_cheese not in ['y', 'n']:
        return 'Invalid choice for extra cheese!'
    return f'Your final bill is ${price}'


your_price = pizza_order_programm()
print(your_price)
