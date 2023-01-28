import random

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_number(x):
    return x % 2 == 0


def ask_answer():
    number = random.randint(0, 100)
    answer = 'no'
    if even_number(number) is True:
        answer = 'yes'
    ask = str(number)
    return ask, str(answer)
