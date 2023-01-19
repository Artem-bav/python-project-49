def gcd___user():
    import prompt  # ожидание ввода
    import random  # случайный выбор
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Find the greatest common divisor of given numbers.''')
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        # answer = 0
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        x = 0
        y = 0
        rez = 0
        if a > b:
            x = a  # x большее число
            y = b
        if a < b:
            x = b
            y = a
        for w in range(y, 0, -1):
            if y % w == 0 and x % w == 0:
                rez = w
                break
        print(f'Question: {x} {y} , (  :) {rez})')
        answer = prompt.string('Your answer: ')  # присв переменной введ ответ
        if rez == int(answer):
            print('Correct!')
            counter_i += 1
        else:
            print(f"""Question: {a} {b}
        Your answer: {answer}
        '{answer}' is wrong answer ;(. Correct answer was '{rez}'.
        Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')

