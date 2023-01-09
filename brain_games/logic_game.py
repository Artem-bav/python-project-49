def hello_name():

    import prompt
    global name  # принудительно обращ к глоб перем name
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What is the result of the expression?''')
    return name


def hello_name_gcd():

    import prompt
    global name  # принудительно обращ к глоб перем name
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Find the greatest common divisor of given numbers.''')
    return name


def hello_name_progression():

    import prompt
    global name  # принудительно обращ к глоб перем name
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What number is missing in the progression?''')
    return name


def hello_name_prime():

    import prompt
    global name  # принудительно обращ к глоб перем name
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if given number is prime. Otherwise answer "no".''')
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


def question_progression():

    import random
    import prompt
    answer = 0
    i = 0
    rez = 0  # переменная для скрытой цифры
    n = 1  # переменная формирования прогрессии
    str_prog = ''
    lenn = random.randint(5, 10)  # случайная длина
    hidden = random.randint(1, lenn)  # случайная скрытая
    start = random.randint(1, 20)  # случайная первая в последователности
    plus = random.randint(2, 5)
    while n < (lenn + 1):
        if n == 1:
            if n == hidden:
                str_prog = str('..') + str(' ')
                rez = start
            else:
                str_prog = str(start) + str(' ')
            next = start + plus
        else:
            if n == hidden:
                str_prog = str(str_prog) + str('..') + str(' ')
                rez = next
            else:
                str_prog = str(str_prog) + str(next) + str(' ')
            next += plus
        n += 1
    print(f'Question: {str_prog}   (  :) {rez})')
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    if rez == int(answer):
        print('Correct!')
        i = 1
    else:
        print(f"""Question: {str_prog}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{rez}'.
Let's try again, {name}!""")
        i = 4
    return i


def question_prime():
    import prompt
    import random
    from math import sqrt
    number = random.randint(2, 1000)  # случайное число
    r = 0
    rez = 'yes'
    if number == 2 or number == 3:
        rez = 'yes'
        r = 1
    elif number % 2 == 0 and number != 2:
        rez = 'no'
        r = 1
    if r == 0:
        for i in range(3, int(number/2), 2):  # for i in range(3, int(sqrt(number)), 2):
            print(i)
            if number % i == 0:
                rez = 'no'
                break
    answer = 0
    print(f'Question: {number}  (  :) {rez})')
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    if rez == str(answer):
        print('Correct!')
        i = 1
    else:
        print(f"""Question: {number}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{rez}'.
Let's try again, {name}!""")
        i = 4
    return i
