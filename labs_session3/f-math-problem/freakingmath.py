from random import *

def calc(x,y,op):

    if op =='+':
        result = x+y
    elif op == '-':
        result = x-y
    elif op == '*':
        result = x*y
    else:
        result = x/y

    return result

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 10)
    y = randint(0, 10)
    op = choice(['+', '+', '-', '*'])
    r = choice([-1, 0, 1])
    res = calc(x, y, op) + r
    return [x, y, op, res]

def check_answer(x, y, op, result, user_choice):
    real_result = calc(x, y, op)
    if result == real_result:
        if user_choice ==True:
            return True
        else:
            return False
    else:
        if user_choice == False:
            return True
        else:
            return False
