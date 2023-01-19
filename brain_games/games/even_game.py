def even_user():
    import prompt  # ожидание ввода
    import random  # случайный выбор
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no".''')
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes':  # число четное
            print('Correct!')
            answer = ''
            counter_i += 1
        elif number % 2 != 0 and answer == 'no':  # число не четное
            print('Correct!')
            answer = ''
            counter_i += 1
        else:
            if answer == 'yes':
                print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
                break
            elif answer == 'no':
                print(f"""'no' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
                break
            else:  # answer != 'yes' end answer != 'no'
                print(f"""\'{answer}\' is wrong answer ;(.
Correct answer was different.
Let's try again, {name}!""")
                break
        if counter_i == 3:
            print(f'Congratulations, {name}!')
