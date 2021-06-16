import random

OPTIONS = ['rock', 'paper', 'scissors']


def get_human_choice():
    print('(1) Rock\n(2) Paper\n(3) Scissors')
    return OPTIONS[int(input('Enter the number of your choice: ')) - 1]


def get_computer_choice():
    return random.choice(OPTIONS)


def print_choices(human_choice, computer_choice):
    print(f'You chose {human_choice.title()}')
    print(f'The computer chose {computer_choice.title()}')


def eval_game_result(human_choice, computer_choice):    
    if human_choice == computer_choice:
        return 'draw'
    elif human_choice == 'rock':
        return 'human' if computer_choice == 'scissors' else 'computer'
    elif human_choice == 'paper':
        return 'human' if computer_choice == 'rock' else 'computer'
    else:
        return 'human' if computer_choice == 'paper' else 'computer'


def compose_output_message(result, human_choice, computer_choice):
    if result == 'draw':
        return 'Draw!'
    elif result == 'human':
        return f'Yes, {human_choice} beat {computer_choice}!'
    else:
        return f'Sorry, {computer_choice} beat {human_choice}'


def print_result(message):
    print(message)


human_choice = get_human_choice()
computer_choice = get_computer_choice()
print_choices(human_choice, computer_choice)
game_result = eval_game_result(human_choice, computer_choice)
print_result(compose_output_message(game_result, human_choice, computer_choice))
