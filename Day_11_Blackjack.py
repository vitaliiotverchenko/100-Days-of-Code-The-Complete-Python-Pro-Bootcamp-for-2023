import random, os


class Blackjack:
    def __init__(self):
        self.deck = self.generate_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False

    def generate_deck(self):
        """
        Generates a deck of playing cards.

        Returns:
            list: A list of dictionaries representing each card in the deck. Each dictionary has two keys: 'value' (a string representing the card's value) and 'suit' (a string representing the card's suit).
        """
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'value': value, 'suit': suit}
                for value in values for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        """
        Pop a card from the deck.

        Returns:
            The popped card.
        """
        return self.deck.pop()

    def calculate_hand_value(self, hand):
        """
        Calculates the value of a hand in a card game.

        Parameters:
            hand (list): A list of dictionaries representing the cards in the hand.
                Each dictionary contains a 'value' key with the value of the card.

        Returns:
            int: The total value of the hand.

        Algorithm:
            1. Create a dictionary 'values' to store the values of each card.
            2. Initialize 'hand_value' as 0.
            3. Iterate through each 'card' in 'hand':
                a. Add the value of the card from 'values' to 'hand_value'.
            4. Count the number of aces in the hand and store it in 'num_aces'.
            5. While 'hand_value' is greater than 21 and 'num_aces' is greater than 0:
                a. Subtract 10 from 'hand_value'.
                b. Decrease 'num_aces' by 1.
            6. Return 'hand_value'.
        """
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        hand_value = sum([values[card['value']] for card in hand])
        num_aces = sum(1 for card in hand if card['value'] == 'A')

        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def print_hand(self, hand, player_name):
        """
        Prints the given hand of cards for a player.

        Args:
            hand (List[Dict[str, Any]]): A list of dictionaries representing the cards in the hand. Each dictionary has two keys: 'value' (str) and 'suit' (str).
            player_name (str): The name of the player.

        Returns:
            None
        """
        print(f"{player_name}'s hand:")
        for card in hand:
            print(f"{card['value']} of {card['suit']}")
        print(f"Total value: {self.calculate_hand_value(hand)}\n")

    def check_blackjack(self, hand):
        """
        Checks if the given hand is a blackjack hand.

        Parameters:
            hand (list): A list of cards representing the hand.

        Returns:
            bool: True if the hand is a blackjack hand, False otherwise.
        """
        return self.calculate_hand_value(hand) == 21

    def check_bust(self, hand):
        """
        Check if the hand value is greater than 21.

        Parameters:
            hand (list): A list of cards representing the hand.

        Returns:
            bool: True if the hand value is greater than 21, False otherwise.
        """
        return self.calculate_hand_value(hand) > 21

    def play_again(self):
        """
        Runs the play again loop, allowing the user to choose whether to play another round or exit the game.

        Returns:
            None
        """
        while True:
            choice = input("Do you want to play again? (yes/no): ").lower()
            if choice == 'yes':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.player_hand.clear()
                self.dealer_hand.clear()
                self.deck = self.generate_deck()
                self.game_over = False
                self.play()
            elif choice == 'no':
                print("Thank you for playing! Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    def play(self):
        """
        Plays a game of blackjack.

        The function initializes the game by dealing two cards to both the player and the dealer.
        It then enters a loop where it displays the player's hand and the dealer's face-up card.
        If the player has a blackjack, the function prints a message and exits the loop.
        If the player busts, the function prints a message and exits the loop.
        If the player chooses to hit, a card is dealt to the player's hand.
        If the player chooses to stand, the function enters a loop where the dealer continues to 
        draw cards until their hand value is 17 or higher. The function then compares the hand values
        of the player and the dealer and determines the outcome of the game (player wins, dealer wins, or draw).

        Parameters:
        None

        Returns:
        None
        """
        # Initial deal
        for _ in range(2):
            self.player_hand.append(self.deal_card())
            self.dealer_hand.append(self.deal_card())

        while not self.game_over:
            self.print_hand(self.player_hand, "Player")
            self.print_hand([self.dealer_hand[0]], "Dealer")

            if self.check_blackjack(self.player_hand):
                print("Blackjack! You win!")
                break

            if self.check_bust(self.player_hand):
                print("Bust! You lose!")
                break

            action = input("Do you want to 'hit' or 'stand'? ").lower()

            if action == 'hit':
                self.player_hand.append(self.deal_card())
            elif action == 'stand':
                while self.calculate_hand_value(self.dealer_hand) < 17:
                    self.dealer_hand.append(self.deal_card())
                self.print_hand(self.dealer_hand, "Dealer")

                if self.check_bust(self.dealer_hand):
                    print("Dealer busts! You win!")
                elif self.calculate_hand_value(self.player_hand) > self.calculate_hand_value(self.dealer_hand):
                    print("You win!")
                elif self.calculate_hand_value(self.player_hand) < self.calculate_hand_value(self.dealer_hand):
                    print("You lose!")
                else:
                    print("It's a draw!")
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")
        # self.play_again()


if __name__ == "__main__":
    game = Blackjack()
    game.play()
    game.play_again()
