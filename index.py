import random

def rock_paper_scissors():
    # define the choices and the rules
    choices = ['rock', 'paper', 'scissors']
    rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    # get the user's choice
    user_choice = input('Choose rock, paper, or scissors: ').lower()
    while user_choice not in choices:
        print('Invalid choice.')
        user_choice = input('Choose rock, paper, or scissors: ').lower()

    # get the computer's choice
    computer_choice = random.choice(choices)
    print('The computer chose', computer_choice)

    # compare the choices and determine the winner
    if user_choice == computer_choice:
        print('It is a tie.')
    elif rules[user_choice] == computer_choice:
        print('You win.')
    else:
        print('You lose.')

# call the function
rock_paper_scissors()
