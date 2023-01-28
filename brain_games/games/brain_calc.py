import random

task = 'What is the result of the expression?'


def calculation(a, b, sign):
    if sign == '+':
        answer = a + b
    elif sign == '-':
        answer = a - b
    else:
        answer = a * b
    return answer


def ask_answer():
    signs = "*+-"
    sign = random.choice(signs)  # случайный выбор знака
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    answer = calculation(a, b, sign)
    ask = (str(a) + ' ' + sign + ' ' + str(b))  # , +' '+ str(answer)
    return ask, str(answer)
