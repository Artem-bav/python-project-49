import prompt

STEPS_TO_VICTORY = 3
WORD_QUESTION = 'Question: '


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.task)  # что нужно сделать
    for _ in range(STEPS_TO_VICTORY):
        ask, answer = game.ask_answer()
        print(WORD_QUESTION + ask)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
        if STEPS_TO_VICTORY == 3:
            print(f"Congratulations, {name}!")
