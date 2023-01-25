import random
a_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer():
    number = random.randint(0, 100)
    answer = 'no'
    if number % 2 == 0:
        answer = 'yes'
    question = (f'Question: {number}')
    return question, str(answer)
