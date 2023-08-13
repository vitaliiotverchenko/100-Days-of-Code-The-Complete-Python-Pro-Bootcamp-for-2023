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
        "water": 1000,
        "milk": 500,
        "coffee": 200,
        "chocolate": 200,
    }

    def display_menu(self):
        message = "Welcome to the coffee machine!\n\nWhat would you like?\n"
        for drink, options in self.MENU.items():
            message += f"{drink}: ${options['cost']}\n"
        return message

    def __init__(self):
        self.money = 0

    def check_resources(self, drink):
        for ingredient, quantity in self.MENU[drink]["ingredients"].items():
            if self.RESOURCES[ingredient] < quantity:
                return False
        return True

    def process_coins(self):
        def get_valid_input(prompt):
            while True:
                choice = input(prompt).lower()
                if choice.isdigit():
                    choice = int(choice)
                    return choice
                else:
                    print('Invalid choice! Please try again.')

        COIN_VALUES = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickels": 0.05,
            "pennies": 0.01,
        }

        total = 0
        for coin, value in COIN_VALUES.items():
            total += int(input(f"How many {coin}? ({value}$): ")) * value
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

                return f"Here is your {drink} ☕. Enjoy! Here's your change: ${change:.2f}"
        else:
            return "Sorry, not enough resources to make the drink."

    def report(self):
        return f"\nCurrent resources:\n\nWater: {self.RESOURCES['water']}ml, Milk: {self.RESOURCES['milk']}ml, Coffee: {self.RESOURCES['coffee']}g, Money: ${self.money:.2f}, Chocolatte: {self.RESOURCES['chocolate']}g"

    def work(self):
        print(logo)
        print(self.display_menu())
        while True:
            choice = input(
                "What would you like? (type 'exit' to stop)\n: ").lower()
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
