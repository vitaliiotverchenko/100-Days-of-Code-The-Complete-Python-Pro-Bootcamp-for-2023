def years_left ():
    """
    Calculate the number of years left based on the user's current age.
    
    """
    years_left = 90 - int(input("What is your current age? "))
    return print(f'You have {years_left * 365} days, {years_left * 52} weeks, and {years_left * 12} months left.')

years_left()