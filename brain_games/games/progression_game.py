def progression_user_hello():
    import prompt  # ожидание ввода
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What number is missing in the progression?''')
    return name


def progression_answer():
    import random  # случайный выбор
    import prompt  # ожидание ввода
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
                rez = start
            else:
                str_prog = str(start) + str(' ')
            next_number = start + plus
        else:
            if n == hidden:
                str_prog = str(str_prog) + str('..') + str(' ')
                rez = next_number
            else:
                str_prog = str(str_prog) + str(next_number) + str(' ')
            next_number += plus
        n += 1
    print(f'Question: {str_prog}')  # (  :) {rez})
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    return rez, str_prog, answer
