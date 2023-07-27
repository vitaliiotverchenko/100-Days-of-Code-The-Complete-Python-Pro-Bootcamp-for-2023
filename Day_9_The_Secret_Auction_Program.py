import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def secret_auction():
    """
    Implements a secret auction program.
    
    This function prompts participants to enter their name and bid for an auction item. It keeps track of the participants and their bids in a dictionary. The function continues to prompt for new bidders until the user indicates there are no more bidders. After all bids have been entered, the function determines the highest bid and the corresponding winner. Finally, it prints the name of the winner and their winning bid.
    
    Parameters:
        None
    
    Returns:
        None
    """
    participants = {}
    print(logo)
    print('Welcome to the secret auction program!')
    answer = 'yes'
    while answer == 'yes':
        name = input('What is your name? ')
        price = int(input('What is your bid? $'))
        participants[name] = price
        answer = input(
            'Are there any other bidders? Type "yes" or "no". ').lower()
        os.system('cls')
    max_bid = 0
    winner = ''
    for bidder, price in participants.items():
        if price > max_bid:
            max_bid = price
            winner = bidder
    return print(f"The winner is {winner} with a bid of ${max_bid}")


secret_auction()
