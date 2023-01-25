from random import randint
from random import choice
#import random  # случайный выбор
#    import prompt  # ожидание ввода


a_task = 'Answer "yes" if the number is even, otherwise answer "no".'



def question_answer():
    import random  # случайный выбор
    import prompt  # ожидание ввода
    number = random.randint(0, 100)
    answer = 'no'
    if number % 2 == 0:
        answer = 'yes'
    question = (f'Question: {number}')
    #answer = prompt.string('Your answer: ')
    return question, str(answer)


