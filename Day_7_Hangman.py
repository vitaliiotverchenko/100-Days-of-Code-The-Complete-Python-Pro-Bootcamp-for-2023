from random_word import RandomWords

r = RandomWords()

hangman_art = {
    6: """
    +---+
    |   |
        |
        |
        |
        |
========= """,
    5: """
    +---+
    |   |
    O   |
        |
        |
        |
========= """,
    4: """
    +---+
    |   |
    O   |
    |   |
        |
        |
========= """,
    3: """
    +---+
    |   |
    O   |
   /|   |
        |
        |
========= """,
    2: """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
========= """,
    1: """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
========= """,
    0: """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
========= """
}


def one_more_time():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            return hangman()
        elif play_again == "no":
            return "Goodbye! Thanks for playing."
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def hangman():
    attempts = 6

    def get_valid_input(prompt: str, valid_choices: list) -> str:
        'check the correct input of the user'
        while True:
            choice = input(prompt).lower()
            if choice in valid_choices:
                return choice
            else:
                print('Invalid choice! Please try again.')

    def check_for_forbidden_chars(input_str):
        for char in input_str:
            if not char.isalpha():
                return False
        return True

    def check_for_one_letter(prompt: str):
        while True:
            letter = input(prompt).lower()
            if len(letter) == 1 and letter.isalpha():
                return letter
            else:
                print(
                    'You should type only one letter, and no symbols! Please, try again!')

    print("\nWelcome to \n ")
    print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  \n''')
    auto_generate = get_valid_input(
        "Do you want to choose a word by yourself, or to auto-generate? Type 'myself' or 'auto' \n", ['myself', 'auto']).lower()
    if auto_generate == 'auto':
        secret_word = r.get_random_word()
    else:
        secret_word = input('Type your own word:\n')
        check = check_for_forbidden_chars(secret_word)
        while check == False:
            secret_word = input(
                "You shouldn't use symbols or numbers! Try again!: \n")
            check = check_for_forbidden_chars(secret_word)

    guessed_letters = []
    while attempts > 0:

        display_word = "".join(
            letter if letter in guessed_letters else "_" for letter in secret_word)

        if "_" not in display_word:
            print(f"Congratulations! You win!\nThe word was: {secret_word}")
            return one_more_time()

        print(f"{hangman_art[attempts]}")
        print(f'The secret word is : {display_word}')
        print("Used letters:", ", ".join(guessed_letters))
        print(f"You have {attempts} attempts")
        guess = check_for_one_letter("Type a letter: \n")

        if guess in guessed_letters:
            print("You've already typed this letter. Try another one. \n")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f'{hangman_art[attempts]}')

    print(f"You fail! The word was: {secret_word}")
    return one_more_time()


if __name__ == "__main__":
    hangman()
