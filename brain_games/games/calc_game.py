def calc_user_hello():
    import prompt  # ожидание ввода
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What is the result of the expression?''')
    return name


def calc_answer():
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
    print(f'Question: {a} {dif_signs} {b}')  # , (  :){c})
    answer = prompt.string('Your answer: ')  # перем->ответ
    return a, b, c, dif_signs, answer
