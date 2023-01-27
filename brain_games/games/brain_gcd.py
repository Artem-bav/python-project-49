import random

task = 'Find the greatest common divisor of given numbers.'


def ask_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    x = 0
    y = 0
    answer = 0
    if a > b:
        x = a  # x большее число
        y = b
    if a < b:
        x = b
        y = a
    for w in range(y, 0, -1):
        if y % w == 0 and x % w == 0:
            answer = w
            break
    ask = (str(x) + ' ' + str(y))  # + ' ' + str(answer)
    return ask, str(answer)
