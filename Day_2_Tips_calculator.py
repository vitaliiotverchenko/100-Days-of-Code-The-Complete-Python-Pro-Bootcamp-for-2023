def tip():
    print('Welcome to the tip calculator.')
    bill = float(input('What was the total bill? $'))
    percent = int(input('What percentage tip would you like to geve? 10, 12, or 15? '))
    people = int(input('How many people to split the bill? '))
    final_amount = "{:.2f}".format((bill + bill * (percent/100)) / people)
    return print(f'Each person should pay: ${final_amount}')
tip()