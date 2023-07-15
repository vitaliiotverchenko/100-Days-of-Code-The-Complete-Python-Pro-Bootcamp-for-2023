# 💪 This is a Difficult Challenge 💪

# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"

# Example Output 1
# Your score is 42, you are alright together.

# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"

# Example Output 2
# Your score is 73.

def love_calculator(name1, name2) -> str:
    dozens = 0
    singles = 0
    string = (name1 + name2).lower()
    for letter in 'true':
        amount = string.count(letter)
        dozens += amount
    for letter in 'love':
        amount = string.count(letter)
        singles += amount
    percent = int(str(dozens) + str(singles))
    if 40 < percent < 50:
        return f"Your score is {percent}%, you are alright together."
    elif percent < 10 or percent > 90:
        return f"Your score is {percent}%, you go together like coke and mentos."
    else:
        return f"Your score is {percent}%."


name1 = input('write your name: ')
name2 = input("write your sweetheart's name: ")
answer = love_calculator(name1, name2)
print(answer)
