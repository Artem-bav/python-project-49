import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def number_prime_test(number):
    return number == 2 or number == 3 or number == 5 or number == 7
    if number % 2 == 0 and number != 2:
        return False
    for i in range(3, int(number / 2), 2):
        if number % i == 0:
            return False
        else:
            return True


def ask_answer():
    number = random.randint(2, 1000)  # случайное число
    ask = str(number)
    if number_prime_test(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return ask, str(answer)
