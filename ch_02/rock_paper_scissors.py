import random

OPTIONS = ['rock', 'paper', 'scissors']

def human_guess():
    print('(1) Rock\n(2) Paper\n(3) Scissors')
    choice = OPTIONS[int(input('Enter the number of your choice: ')) - 1]
    print(f'You chose {choice}')
    return choice


def computer_guess():
    choice = random.choice(OPTIONS)
    print(f'The computer chose {choice}')
    return choice


def result(human_choice, computer_choice):    
    if human_choice == computer_choice:
        return 'draw'
    elif human_choice == 'rock':
        return 'human' if computer_choice == 'scissors' else 'computer'
    elif human_choice == 'paper':
        return 'human' if computer_choice == 'rock' else 'computer'
    else:
        return 'human' if computer_choice == 'paper' else 'computer'


def output_message(result, human_choice, computer_choice):
    if result == 'draw':
        return 'Draw!'
    elif result == 'human':
        return f'Yes, {human_choice} beat {computer_choice}!'
    else:
        return f'Sorry, {computer_choice} beat {human_choice}'


def share_result(message):
    print(message)


human_choice = human_guess()
computer_choice = computer_guess()
game_result = result(human_choice, computer_choice)
share_result(output_message(game_result, human_choice, computer_choice))
