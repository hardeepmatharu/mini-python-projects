import random

user_wins = 0
computer_wins = 0
options = ['rock','paper', 'scissors']

while True:
    user_input = input('Please enter Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    # 0 for rock, 1 for paper and 2 for scissors
    computer_pick = options[random_number]
    print('Computer picked: ',computer_pick)

    if user_input == 'rock' and computer_pick == 'scissors':
        user_wins += 1
        print('You won!')
        continue
    elif user_input == 'scissors' and computer_pick == 'paper':
        user_wins += 1
        print('You won!')
        continue
    elif user_input == 'paper' and computer_pick == 'rock':
        user_wins += 1
        print('You won!')
        continue
    else:
        computer_wins += 1
        print('Computer won!')
print('Computer won:', computer_wins , 'times.')
print('You won:', user_wins, 'times.') 
print('Goodbye!')