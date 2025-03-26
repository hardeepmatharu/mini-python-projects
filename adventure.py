user_name = input('Type your name: ').capitalize()
print('Welcome', user_name, 'to this adventurous world!')

answer = input(user_name+','+'you are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go left or right: ').lower()
print(answer)

if answer == 'left':
   answer = input('You come to a river. You can either walk around or swim. Enter walk to walk around and swim to swim: ').lower()
   if answer == 'walk':
     print('You walked many miles across the river and you ran out of water and you lost the game.')
   elif answer == 'swim':
     print('You swam across the and you were eaten by an alligator. You lost.')
   else:
     print('Not a valid option. You lose.')

elif answer == 'right':
  pass
else:
  print('Not a valid option. You lose.')