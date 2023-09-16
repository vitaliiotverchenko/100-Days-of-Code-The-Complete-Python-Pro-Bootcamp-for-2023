import pandas
PATH = "Day_26_NATO_Alphabet/nato_phonetic_alphabet.csv"
alphabet = pandas.read_csv(PATH)
dict_alphabet = {row.letter: row.code for (letter, row) in alphabet.iterrows()}

name = input("Enter your name: ").upper()
name_list = [dict_alphabet[letter] for letter in name]
print(name_list)
# Loop through rows of a data frame
# for (index, row) in alphabet.iterrows():
#     print(row.letter, row.code)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
