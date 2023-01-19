def progression___user():
    import prompt  # ожидание ввода
    import random  # случайный выбор
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What number is missing in the progression?''')
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        answer = 0
        counter_i = 0
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
        print(f'Question: {str_prog}   (  :) {rez})')
        answer = prompt.string('Your answer: ')  # присв переменной введ ответ
        if rez == int(answer):
            print('Correct!')
            counter_i += 1
        else:

            print(f"""Question: {str_prog}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{rez}'.
Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')