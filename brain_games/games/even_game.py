def even_user_hello():
    import prompt  # ожидание ввода
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no".''')
    return name


def even_answer():
    import random  # случайный выбор
    import prompt  # ожидание ввода
    number = random.randint(0, 100)
    correct_answer = 'no'
    if number % 2 == 0:
        correct_answer = 'yes'
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    return number, answer, correct_answer
