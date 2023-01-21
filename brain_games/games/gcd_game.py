def gcd_user_hello():
    import prompt  # ожидание ввода
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}!
Find the greatest common divisor of given numbers.''')
    return name


def gcd_answer():
    import random  # случайный выбор
    import prompt  # ожидание ввода
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
    print(f'Question: {x} {y}')  # (  :) {rez})
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    return a, b, rez, answer
