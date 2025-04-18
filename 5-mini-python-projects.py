'''1. Circle Area Calculator

Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504'''
from math import pi

radius = float(input('Enter the radius of circle: '))
print(radius, type(radius))

area = pi * radius**2
print('Area of a circle is ', area)


'''2. Reverse Full Name
Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.'''

first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
print('First name: ', first_name)
print('Last name:', last_name)

print('Reverse order')
reverse_first = first_name[::-1]
reverse_last = last_name[::-1]

print(reverse_first + ' ' + reverse_last)


'''3. List and Tuple Generator

Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

user_input = input('Enter numbres separated by comma. ')
print('User input values ',user_input)

new_list = user_input.split(',')
print('New List', new_list)

# convert list to tuple
new_tuple = tuple(new_list)
print('New Tuple', new_tuple)




'''4. File Extension Extractor
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.ipynb
Output : ipynb'''


file_name = input('Enter the file name with extension: ')
print('File name: ', file_name)

new_arr = file_name.split('.')
print('File Extesion is ', repr(new_arr[-1]))  #The repr() function returns a string containing a printable representation of an object.


'''5. First and Last Colors

Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]'''

color_list = ['Red', 'Green', 'White', 'Black']
print('First color is ', color_list[0])
print('Last color is ', color_list[-1])