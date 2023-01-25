from random import randint
from random import choice


a_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_answer():
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
    question = (f'Question: {number}  (  :) {answer}' )  # (  :) {rez})
    return question, str(answer)