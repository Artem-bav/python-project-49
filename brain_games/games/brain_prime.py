import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask_answer():
    r = 0  # есть ли результат, 1 - есть
    answer = 'no'
    number = random.randint(2, 1000)  # случайное число
    if number == 2 or number == 3 or number == 5 or number == 7:
        answer = 'yes'  # число простое
        r = 1
    if number % 2 == 0 and number != 2:
        answer = 'no'
        r = 1
    if r == 0:
        for i in range(3, int(number / 2), 2):
            if number % i == 0:
                answer = 'no'
                break
            else:
                answer = 'yes'
    ask = (str(number) + str(answer))  # (  :) {rez})
    return ask, str(answer)
