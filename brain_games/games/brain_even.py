import random

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_answer():
    number = random.randint(0, 100)
    answer = 'no'
    if number % 2 == 0:
        answer = 'yes'
    ask = (str(number))
    return ask, str(answer)
