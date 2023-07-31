import random

class Blackjack:
    def __init__(self):
        self.deck = self.generate_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False

    def generate_deck(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'value': value, 'suit': suit} for value in values for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def calculate_hand_value(self, hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        hand_value = sum([values[card['value']] for card in hand])
        num_aces = sum(1 for card in hand if card['value'] == 'A')

        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def print_hand(self, hand, player_name):
        print(f"{player_name}'s hand:")
        for card in hand:
            print(f"{card['value']} of {card['suit']}")
        print(f"Total value: {self.calculate_hand_value(hand)}\n")

    def check_blackjack(self, hand):
        return self.calculate_hand_value(hand) == 21

    def check_bust(self, hand):
        return self.calculate_hand_value(hand) > 21

    def play(self):
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

if __name__ == "__main__":
    game = Blackjack()
    game.play()
