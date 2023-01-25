import random
import prompt
a_task = 'What number is missing in the progression?'


def question_answer():
    answer = 0
    rez = 0  # переменная для скрытой цифры
    n = 1  # переменная формирования прогрессии
    str_prog = ''
    lenn = random.randint(5, 10)  # случайная длина
    hidden = random.randint(1, lenn)  # случайная скрытая
    start = random.randint(1, 20)  # случайная первая в последователности
    plus = random.randint(2, 5)
    next_number = 0
    while n < (lenn + 1):
        if n == 1:
            if n == hidden:
                str_prog = str('..') + str(' ')
                answer = start
            else:
                str_prog = str(start) + str(' ')
            next_number = start + plus
        else:
            if n == hidden:
                str_prog = str(str_prog) + str('..') + str(' ')
                answer = next_number
            else:
                str_prog = str(str_prog) + str(next_number) + str(' ')
            next_number += plus
        n += 1
    question = (f'Question: {str_prog}  (  :) {answer} ')  # (  :) {rez})
    return question, str(answer)
