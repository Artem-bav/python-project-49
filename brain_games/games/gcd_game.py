from random import randint
from random import choice
#import random  # случайный выбор
#    import prompt  # ожидание ввода


a_task = 'Find the greatest common divisor of given numbers.'



def question_answer():
    import random  # случайный выбор
    import prompt  # ожидание ввода
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    x = 0
    y = 0
    answer = 0
    if a > b:
        x = a  # x большее число
        y = b
    if a < b:
        x = b
        y = a
    for w in range(y, 0, -1):
        if y % w == 0 and x % w == 0:
            answer = w
            break
    question = (f'Question: {x} {y}  (  :) {answer}   ')  # (  :) {rez})
    #print(f'Question: {x} {y}')  # (  :) {rez})
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    return question, str(answer)