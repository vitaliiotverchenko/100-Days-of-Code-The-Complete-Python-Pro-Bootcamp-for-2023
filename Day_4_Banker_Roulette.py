# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!


import random as r

def banker_roulette(names:list) -> str:
    return f'{r.choice(names)} is going to buy the meal today!'

names = input("Give me everybody's names, separated by a comma. ").strip().split(', ')

print(banker_roulette(names))