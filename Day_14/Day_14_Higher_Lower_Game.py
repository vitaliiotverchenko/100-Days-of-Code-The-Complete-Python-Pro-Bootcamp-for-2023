# The game where user have to guess whom have more followers on Instagram.


import random
import os
from Day_14_Game_Data import data
from Day_14_art import logo, vs


class Player:
    def __init__(self):
        self.score = 0


class HigherLowerGame:
    def __init__(self):
        self.player = Player()
        self.is_game_over = False
        self.person1 = None
        self.person2 = None

    def choose_characters(self):
        if self.player.score == 0:
            self.person1 = random.choice(data)
            self.person2 = random.choice(data)
        elif self.player.score > 0:
            self.person1 = self.person2
            self.person2 = random.choice(data)
        while self.person1 == self.person2:
            self.person2 = random.choice(data)

    def clear_terminal(self):
        os.system('cls')  # for Windows systems

    def get_user_guess(self):
        print(
            f"Compare A: {self.person1['name']}, {self.person1['description']}, from {self.person1['country']}.")
        print(vs)
        print(
            f"Against B: {self.person2['name']}, {self.person2['description']}, from {self.person2['country']}.")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_guess == 'a' or user_guess == 'b':
            return user_guess
        else:
            print("Invalid input. Please type 'A' or 'B'.")
            return self.get_user_guess()

    def play_again(self):
        play_again = input(
            "Do you want to play again? Type 'y' or 'n': ").lower()
        if play_again in ('y', 'yes', 'yeah', 'yup', 'yep', 'ya'):
            self.is_game_over = False
            self.player.score = 0
            self.play_game()
        else:
            print("Thanks for playing! See you again!")
            exit(0)

    def play_round(self):
        self.choose_characters()
        user_guess = self.get_user_guess()

        a_followers = self.person1['follower_count']
        b_followers = self.person2['follower_count']

        if (user_guess == 'a' and a_followers > b_followers) or (user_guess == 'b' and b_followers > a_followers):
            self.player.score += 1
            self.clear_terminal()
            print(f"Correct! Your current score is: {self.player.score} \n")
        else:
            self.is_game_over = True
            self.clear_terminal()
            print(
                f"\nSorry, that's wrong. Your final score is: {self.player.score}")

    def play_game(self):
        self.clear_terminal
        print(logo)
        print("Welcome to Higher - Lower Game!       ")
        print("--------------------------")
        while not self.is_game_over:
            self.play_round()
            input("Press Enter to continue...")
        self.play_again()


if __name__ == "__main__":
    game = HigherLowerGame()
    game.play_game()
