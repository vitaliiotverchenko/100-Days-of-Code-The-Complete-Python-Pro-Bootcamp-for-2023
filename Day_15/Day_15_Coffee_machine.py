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
        "water": 500,
        "milk": 300,
        "coffee": 50,
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
            total += get_valid_input(f"How many {coin}? ({value}$): ") * value
        return total

    def make_coffee(self, drink):
        enough_resources = self.check_resources(drink)
        if not enough_resources:
            required_resources = self.MENU[drink]["ingredients"]
            insufficient_resources = {ingredient: quantity - self.RESOURCES.get(ingredient, 0) for ingredient, quantity in required_resources.items() if self.RESOURCES.get(ingredient, 0) < quantity}
            resource_info = "\n".join([f"Need {quantity} more {ingredient.capitalize()}" for ingredient, quantity in insufficient_resources.items()])
            available_drinks = [d for d in CoffeeMachine.MENU if self.check_resources(d)]
            available_info = ", ".join(available_drinks)
            if len(available_drinks) < 3:
                available_info = "No available drinks"
            return f"Sorry, not enough resources to make {drink}. \n{resource_info}. You can make: {available_info}"
        else:
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


    def report(self):
        return f"\nCurrent resources:\n\nWater: {self.RESOURCES['water']}ml, Milk: {self.RESOURCES['milk']}ml, Coffee: {self.RESOURCES['coffee']}g, Chocolatte: {self.RESOURCES['chocolate']}g, Money: ${self.money:.2f}"

    def work(self):
        print(logo)
        print(self.display_menu())
        while True:
            choice = input(
                "What would you like? (type 'off' to stop)\n: ").lower()
            if choice == "report":
                print(self.report())
            elif choice in CoffeeMachine.MENU.keys():
                result = self.make_coffee(choice)
                print(result)
            elif choice == "off":
                break
            else:
                print("Invalid input. Please choose a valid option.")


coffee_machine = CoffeeMachine()

coffee_machine.work()
