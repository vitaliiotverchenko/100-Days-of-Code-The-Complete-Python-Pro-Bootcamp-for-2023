from Day_15_Coffee_machine_logo import logo

class CoffeeMachine:
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },

        "americano": {
            "ingredients": {
                "water": 100,
                "coffee": 20,
            },
            "cost": 2.0,
        },

        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        },
        "hot chocolate": {
            "ingredients": {
                "water": 250,
                "coffee": 0,
                "milk": 50,
                "chocolate": 100,
            },
            "cost": 1.5,
        },
    }

    RESOURCES = {
        "water": 5000,
        "milk": 2500,
        "coffee": 1000,
        "chocolate": 1000,
    }

    def display_menu(self):
        # drink_options = ", ".join(self.MENU.keys())
        # return f"Welcome to the coffee machine!\nWhat would you like?\n{drink_options}\n"
        message = f"Welcome to the coffee machine!\n\nWhat would you like?\n"
        for drink, options in self.MENU.items():
            message += f"{drink}: ${options['cost']}\n"
        return message

    def __init__(self):
        self.money = 0

    def check_resources(self, drink):
        """
        Check if there are enough resources to make a given drink.

        Parameters:
            self (object): The instance of the class.
            drink (str): The name of the drink to check.

        Returns:
            bool: True if there are enough resources, False otherwise.
        """
        for ingredient, quantity in self.MENU[drink]["ingredients"].items():
            if self.RESOURCES[ingredient] < quantity:
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("How many quarters? (0.25$): ")) * 0.25
        total += int(input("How many dimes? (0.10$): ")) * 0.10
        total += int(input("How many nickels? (0.05$): ")) * 0.05
        total += int(input("How many pennies? (0.01$): ")) * 0.01
        return total

    def make_coffee(self, drink):
        if self.check_resources(drink):
            cost = self.MENU[drink]["cost"]
            coins = self.process_coins()

            if coins < cost:
                return "Sorry, that's not enough money. Money refunded."
            else:
                self.money += cost
                change = coins - cost

                for ingredient, quantity in self.MENU[drink]["ingredients"].items():
                    self.RESOURCES[ingredient] -= quantity

                return f"Here is your {drink}. Enjoy! Here's your change: ${change:.2f}"
        else:
            return "Sorry, not enough resources to make the drink."

    def report(self):
        return f"Water: {self.RESOURCES['water']}ml, Milk: {self.RESOURCES['milk']}ml, Coffee: {self.RESOURCES['coffee']}g, Money: ${self.money:.2f}"

    def work(self):
        print(logo)
        print(self.display_menu())
        while True:
            choice = input("What would you like?\n: ").lower()
            if choice == "report":
                print(self.report())
            elif choice in CoffeeMachine.MENU.keys():
                result = self.make_coffee(choice)
                print(result)
            elif choice == "exit":
                break
            else:
                print("Invalid input. Please choose a valid option.")


coffee_machine = CoffeeMachine()

coffee_machine.work()
# while True:
#     choice = input("What would you like?\nespresso - 1.50$\nlatte - 2.50$\ncappuccino - 3.00$\n: ").lower()

#     if choice == "report":
#         print(coffee_machine.report())
#     elif choice in ["espresso", "latte", "cappuccino"]:
#         result = coffee_machine.make_coffee(choice)
#         print(result)
#     else:
#         print("Invalid input. Please choose a valid option.")
