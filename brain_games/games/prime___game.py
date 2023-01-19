def prime___user():
    import prompt  # ожидание ввода
    import random  # случайный выбор
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if given number is prime. Otherwise answer "no".''')
    counter_i = 0  # счетчик правильных ответов
    number = random.randint(2, 1000)  # случайное число
    r = 0 # есть ли результат, 1 - есть
    rez = 'no'
    while counter_i <= 2:
        if number == 2 or number == 3 or number == 5 or number == 7:
            rez = 'yes'  # число простое
            r = 1
        if number % 2 == 0 and number != 2:
            rez = 'no'
            r = 1
        if r == 0:
            for i in range(3, int(number / 2), 2):
                print(i)
                print(int(number / 2))
                print(number % i)
                if number % i == 0:
                    rez = 'no'
                    break
                else:
                    rez = 'yes'
        answer = ''
        print(f'Question: {number}  (  :) {rez})')
        answer = prompt.string('Your answer: ')  # присв переменной введ ответ
        if rez == str(answer):
            print('Correct!')
            counter_i += 1
        else:
            print(f"""Question: {number}
        Your answer: {answer}
        '{answer}' is wrong answer ;(. Correct answer was '{rez}'.
        Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')
