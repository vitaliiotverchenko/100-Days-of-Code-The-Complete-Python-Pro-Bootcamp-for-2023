# Number guessing game

import random
logo = ''''                 __   ___  __      __        ___  __   __          __      __              ___ 
|\ | |  |  |\/| |__) |__  |__)    / _` |  | |__  /__` /__` | |\ | / _`    / _`  /\   |\/| |__  
| \| \__/  |  | |__) |___ |  \    \__> \__/ |___ .__/ .__/ | | \| \__>    \__> /~~\  |  | |___ 
                                                                                               '''


class GuessingGame:
    EASY_ATTEMPTS = 10
    HARD_ATTEMPTS = 5

    def __init__(self):
        self.secret_number = 0
        self.max_attempts = 0

    @staticmethod
    def get_correct_input(prompt, options):
        while True:
            user_input = input(prompt).lower()
            if user_input in options:
                return user_input
            print("Invalid input. Please enter a valid option.")

    def choose_difficulty(self):
        difficulty = self.get_correct_input(
            "\nChoose difficulty (easy/hard): ", ('easy', 'hard', 'e', 'h')).lower()
        if difficulty in ('easy', 'e'):
            self.max_attempts = GuessingGame.EASY_ATTEMPTS
        elif difficulty in ('hard', 'h'):
            self.max_attempts = GuessingGame.HARD_ATTEMPTS

    def generate_secret_number(self):
        self.secret_number = random.randint(1, 100)

    def play_again(self):
        play_again = self.get_correct_input(
            "\nPlay again? (yes/no): ", ('yes', 'no', 'y', 'n')).lower()
        if play_again in ('yes', 'y'):
            self.play()
        elif play_again in ('no', 'n'):
            print("Goodbye!")

    def play(self):
        print(logo)
        print("Welcome to the Number Guessing Game!")
        self.choose_difficulty()
        self.generate_secret_number()

        attempts = 0
        while attempts < self.max_attempts:
            try:
                guess = int(input("\nEnter your guess (1-100): "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            attempts += 1
            if guess == self.secret_number:
                print(
                    f"Congratulations! You guessed the secret number {self.secret_number} in {attempts} attempts!")
                break
            elif guess < self.secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

            print(f"Attempts left: {self.max_attempts - attempts}")

        else:
            print(
                f"Sorry, you have run out of attempts. The secret number was {self.secret_number}.")
        self.play_again()


if __name__ == "__main__":
    game = GuessingGame()
    game.play()
