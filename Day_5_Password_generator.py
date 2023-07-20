#Password Generator Project

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


import random
import string

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))



def generate_password(letters:int, symbols:int, numbers:int) ->str:
    all_letters = ''.join(random.choice(string.ascii_letters) for _ in range(letters))
    all_symbols = ''.join(random.choice(string.punctuation) for _ in range(symbols))
    all_numbers = ''.join(random.choice(string.digits) for _ in range(numbers))
    
    password_list = list(all_letters + all_symbols + all_numbers)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    return shuffled_password


# Перевірка мінімальної довжини пароля
min_length = num_letters + num_symbols + num_numbers
if min_length < 6:
    print("Error: Password must be at least 6 characters long.")
else:
    password = generate_password(num_letters, num_symbols, num_numbers)
    print(password)
