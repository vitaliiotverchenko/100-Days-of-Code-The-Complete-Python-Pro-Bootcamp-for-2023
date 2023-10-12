import pandas
PATH = "Day_26_NATO_Alphabet/nato_phonetic_alphabet.csv"
alphabet = pandas.read_csv(PATH)
dict_alphabet = {row.letter: row.code for (letter, row) in alphabet.iterrows()}

def generate_phonetic():
    while True:
        try:
            name = input("Enter your name: ").upper()
            name_list = [dict_alphabet[letter] for letter in name]
            print(name_list)
            break
        except KeyError:
            print("Please use only letters from the alphabet")

generate_phonetic()
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
