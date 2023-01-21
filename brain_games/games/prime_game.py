def prime_user_hello():
    import prompt  # ожидание ввода
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Answer "yes" if given number is prime. Otherwise answer "no".''')
    return name


def prime_answer():
    import prompt  # ожидание ввода
    import random  # случайный выбор
    r = 0  # есть ли результат, 1 - есть
    rez = 'no'
    number = random.randint(2, 1000)  # случайное число
    if number == 2 or number == 3 or number == 5 or number == 7:
        rez = 'yes'  # число простое
        r = 1
    if number % 2 == 0 and number != 2:
        rez = 'no'
        r = 1
    if r == 0:
        for i in range(3, int(number / 2), 2):
            if number % i == 0:
                rez = 'no'
                break
            else:
                rez = 'yes'
        answer = ''
    print(f'Question: {number}')  # (  :) {rez})
    answer = prompt.string('Your answer: ')  # присв перем ответ
    return rez, number, answer
