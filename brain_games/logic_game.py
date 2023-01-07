def hello_name():

    import prompt
    global name  # принудительно обращаемся к глобальной переменной name
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What is the result of the expression?''')
    return name


def hello_name_gcd():

    import prompt
    global name  # принудительно обращаемся к глобальной переменной name
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Find the greatest common divisor of given numbers.''')
    return name


def question_calc():

    import random
    import prompt
    answer = 0
    i = 0
    signs = "*+-"
    dif_signs = random.choice(signs)  # случайный выбор знака
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if dif_signs == '+':
        c = a + b
    elif dif_signs == '-':
        c = a - b
    else:
        c = a * b
    print(f'Question: {a} {dif_signs} {b} , (  :) {c})')
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    if c == int(answer):
        print('Correct!')
        i = 1
    else:
        print(f"""Question: {a} {dif_signs} {b}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{c}'.
Let's try again, {name}!""")
        i = 4
    dif_signs = ''  # очистка переменной
    return i


def question_gcd():

    import random
    import prompt
    answer = 0
    i = 0
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    z = x % y
    rez = y
    while z > 0:
        x = y
        y = z
        z = x % y
        rez = y
    print(f'Question: {x} {y} , (  :) {rez})')
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    if rez == int(answer):
        print('Correct!')
        i = 1
    else:
        print(f"""Question: {a} {b}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{rez}'.
Let's try again, {name}!""")
        i = 4
    return i
