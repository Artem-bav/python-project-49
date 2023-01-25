import prompt
from brain_games.cli import welcome_user

counter_i = 3


def go_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.a_task)  # что нужно сделать
    for _ in range(counter_i):
        question, answer = game.question_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
        elif user_answer == answer:
            print('Correct!')
        if counter_i == 3:
            print(f"Congratulations, {name}!")
