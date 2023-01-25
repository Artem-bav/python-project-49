import random
import prompt
a_task = 'Find the greatest common divisor of given numbers.'


def question_answer():
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
    answer = prompt.string('Your answer: ')  # присв переменной введ ответ
    return question, str(answer)
