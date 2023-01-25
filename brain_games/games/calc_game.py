import random
a_task = 'What is the result of the expression?'


def question_answer():

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
    question = (f'Question: {a} {dif_signs} {b}')  # , (  :){c})
    return question, str(answer)
