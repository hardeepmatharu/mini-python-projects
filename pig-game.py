import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input('Enter the number of players(2 - 4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Number of players must be between 2 -4')
    else:
        print('Enter the valid number')
print('players', players)

max_score = 50
players_score = [0 for _ in range(players)]
print('Players:', players)

number = 12345
print(str(number))
for digit in 'hello':
    print(digit)
# list_created = [int(digit) for digit in str(number)]
# print(list_created)