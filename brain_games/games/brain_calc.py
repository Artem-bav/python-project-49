import random

task = 'What is the result of the expression?'


def ask_answer():
    signs = "*+-"
    sign = random.choice(signs)  # случайный выбор знака
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if sign == '+':
        answer = a + b
    elif sign == '-':
        answer = a - b
    else:
        answer = a * b
    ask = (str(a) + ' ' + sign + ' ' + str(b))  # , (  :){answer})
    return ask, str(answer)
