#my first version , before impoving
import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
variants = (rock, paper, scissors)
#Rock wins against scissors; paper wins against rock; and scissors wins against paper.

def rock_paper_scissors(choose: str) -> str:
    print('Your choice is: ')
    if choose in 'paper':
        choose = paper
        print(paper)
    elif choose in 'rock':
        choose = rock
        print(rock)
    else:
        choose = scissors
        print(scissors)
    print('Computer chose:')
    pc_choose = r.choice(variants)
    print(pc_choose)
    while choose == pc_choose:
        choose = input("That's a draw! Try again: ")
        rock_paper_scissors(choose)
    if choose in 'rock' and pc_choose == scissors:
        return 'You win!'
    else:
        return 'You lose!'
        

choice = input('What do you chose? Rock, paper, scissors? \n').lower()
print(rock_paper_scissors(choice))
