from random import randint
from random import choice
#import random  # случайный выбор
#    import prompt  # ожидание ввода


a_task = 'What is the result of the expression?'



def question_answer():
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
        answer = a + b
    elif dif_signs == '-':
        answer = a - b
    else:
        answer = a * b
    question = (f'Question: {a} {dif_signs} {b} , (  :){answer}')  # , (  :){c})

    # answer = prompt.string('Your answer: ')  # перем->ответ
    return question, str(answer)
