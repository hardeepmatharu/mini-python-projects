user_name = input('Type your name: ').capitalize()
print('Welcome', user_name, 'to this adventurous world!')

answer = input(user_name+','+'you are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go left or right: ').lower()
print(answer)

if answer == 'left':
   answer = input('You come to a river. You can either walk around or swim. Enter walk to walk around and swim to swim: ').lower()
   if answer == 'walk':
     print('You walked many miles across the river and you ran out of water and you lost the game.')
   elif answer == 'swim':
     print('You swam across the river and you were eaten by an alligator. You lost.')
   else:
     print('Not a valid option. You lose.')

elif answer == 'right':
    answer = input('You come to a bridge, it is wobbly. You want to cross it or go back(cross/back)? ')
    if answer == 'cross':
      print('You crossed the bridge and you meet a stranger. You talk to stranger. yes/no? ')
      if answer == 'yes':
        print('You talked to a stranger and he gave you gold and you WIN!')
      elif answer == 'no':
        print('You ignored the stranger and he got offended and you lose.')
      else:
        print('Not a valid option. You lose.')
    elif answer == 'back':
      print('You go back. You lost.')
    else:
      print('Not a valid option. You lose.')
else:
  print('Not a valid option. You lose.')
print('Thank you',user_name, 'for playing this game!')