from random import randint
from random import choice
#import random  # случайный выбор
#    import prompt  # ожидание ввода


a_task = 'What is the result of the expression?'



def calc_question_answer():
    import random  # случайный выбор
    import prompt  # ожидание ввода
    signs = "*+-"
    dif_signs = ''
    dif_signs = random.choice(signs)  # случайный выбор знака
    a = random.randint(0, 100)
    print(a)
    b = random.randint(0, 100)
    print(b)
    if dif_signs == '+':
        c = a + b
    elif dif_signs == '-':
        c = a - b
    else:
        c = a * b
    question = (f'Question: {a} {dif_signs} {b}')  # , (  :){c})
    answer = prompt.string('Your answer: ')  # перем->ответ
    return question, answer
