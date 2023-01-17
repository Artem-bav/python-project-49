def calc___game():


    import prompt  # ожидание ввода
    import random  # случайный выбор
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
What is the result of the expression?''')
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        signs = "*+-"
        dif_signs = ''
        # answer = 0
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
            counter_i += 1
        else:
            print(f"""Question: {a} {dif_signs} {b}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{c}'.
Let's try again, {name}!""")
            # i = 4
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')