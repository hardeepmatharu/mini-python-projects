print("Welcome to computer quiz!")
playing = input("Do you want to play? ")
score = 0
if playing.strip().lower() != 'yes':
    quit()
print('Lets play the game! :)')
answer = input('What does CPU stand for?: ')
if answer.strip().lower() == 'central processing unit':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

answer = input('What does RAM stand for?: ')
if answer.strip().lower() == 'random access memory':
    print('Correct!')
    score += 1

else: 
    print('Incorrect!')
answer = input('What does ROM stand for?: ')
if answer.strip().lower() == 'read only memory':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score/3) * 100 ) + '%.')