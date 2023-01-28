import random

task = 'What number is missing in the progression?'


def sequence_generator(lenn, start_number, plus, hidden):
    element_number = 1  # переменная формирования прогрессии
    while element_number < (lenn + 1):
        if element_number == 1:
            if element_number == hidden:
                str_prog = str('..') + str(' ')
                answer = start_number
            else:
                str_prog = str(start_number) + str(' ')
            next_number = start_number + plus
        else:
            if element_number == hidden:
                str_prog = str(str_prog) + str('..') + str(' ')
                answer = next_number
            else:
                str_prog = str(str_prog) + str(next_number) + str(' ')
            next_number += plus
        element_number += 1
    return str_prog, answer


def ask_answer():
    lenn = random.randint(5, 10)  # случайная длина
    start_number = random.randint(1, 20)  # случайная первая
    plus = random.randint(2, 5)
    hidden = random.randint(1, lenn)  # случайная скрытая
    ask, answer = sequence_generator(lenn, start_number, plus, hidden)
    return ask, str(answer)
