import random
import time


OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 4




print('Lets play the math game')
print('--------------------------')
start_time = time.time()

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr) # eval evaluates the expression and gives the answer
    return expr,answer

for i in range(TOTAL_PROBLEMS):    
    expr,answer = generate_problem()
    while True:
        # ask user about the answer
        guess = input('Problem #'+ str(i+1) + ': ' + expr + ' = ')
        if guess == str(answer):
            end_time = time.time()
            break
time_finished = round(end_time - start_time, 2)   

print('--------------------')
print('Nice Work! you completed in ',time_finished, 'seconds!')
