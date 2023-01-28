import random

task = 'Find the greatest common divisor of given numbers.'


def divisor_search(x, y):
    if x > y:
        big_number = x  # x большее число
        small_number = y
    if x < y:
        big_number = y
        small_number = x
    for divider in range(small_number, 0, -1):
        if small_number % divider == 0 and big_number % divider == 0:
            return divider


def ask_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    answer = divisor_search(a, b)
    ask = (str(a) + ' ' + str(b))  # + ' ' + str(answer)
    return ask, str(answer)
