def calc_go():
    from brain_games.games import calc_game
    name = calc_game.calc_user_hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        a, b, c, dif_signs, answer = calc_game.calc_answer()
        if str(c) == answer:
            print('Correct!')
            counter_i += 1
        else:
            print(f"""Question: {a} {dif_signs} {b}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{c}'.
Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')


def even_go():
    from brain_games.games import even_game
    name = even_game.even_user_hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        number, answer, correct_answer = even_game.even_answer()
        if str(correct_answer) == answer:
            print('Correct!')
            counter_i += 1
        else:
            print(f"""Question: {number}'
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')
        answer = ''


def gcd_go():
    from brain_games.games import gcd_game
    name = gcd_game.gcd_user_hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        a, b, rez, answer = gcd_game.gcd_answer()
        if str(rez) == answer:
            print('Correct!')
            counter_i += 1
        else:
            print(f"""Question: {a} {b}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{rez}'.
Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')


def prime_go():
    from brain_games.games import prime_game
    name = prime_game.prime_user_hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        rez, number, answer = prime_game.prime_answer()
        if str(rez) == answer:
            print('Correct!')
            counter_i += 1
        else:
            print(f"""Question: {number}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{rez}'.
Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')


def progression_go():
    from brain_games.games import progression_game
    name = progression_game.progression_user_hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        rez, str_prog, answer = progression_game.progression_answer()
        if str(rez) == answer:
            print('Correct!')
            counter_i += 1
        else:
            print(f"""Question: {str_prog}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{rez}'.
Let's try again, {name}!""")
            break
        if counter_i == 3:
            print(f'Congratulations, {name}!')
