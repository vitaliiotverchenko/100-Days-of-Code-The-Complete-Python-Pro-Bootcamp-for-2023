def tip():
    print('Welcome to the tip calculator.')
    bill = float(input('What was the total bill? $'))
    people = int(input('How many people to split the bill? '))
    percent = int(input('What percentage tip would you like to geve? 10, 12, or 15? '))
    return print(f'Each person should pay: ${round((bill+ bill * percent/100) / people, 1)}')
tip()