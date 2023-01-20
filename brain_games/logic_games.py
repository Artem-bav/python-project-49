def calc__go():
    from brain_games.games import calc__game
    name = calc__game.calc__user__hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        a, b, c, dif_signs, answer = calc__game.calc__answer()
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
            
            
def even__go():
    from brain_games.games import even__game
    name = even__game.even__user__hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        number, answer = even__game.even__answer()
        if number % 2 == 0 and answer == 'yes':  # число четное
            print('Correct!')
            answer = ''
            counter_i += 1
        elif number % 2 != 0 and answer == 'no':  # число не четное
            print('Correct!')
            answer = ''
            counter_i += 1
        else:
            if answer == 'yes':
                print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
                break
            elif answer == 'no':
                print(f"""'no' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
                break
            else:  # answer != 'yes' end answer != 'no'
                print(f"""\'{answer}\' is wrong answer ;(.
Correct answer was different.
Let's try again, {name}!""")
                break
        if counter_i == 3:
            print(f'Congratulations, {name}!')


def gcd__go():
    from brain_games.games import gcd__game
    name = gcd__game.gcd__user__hello()
    counter_i = 0  # счетчик правильных ответов
    while counter_i <= 2:
        a, b, rez, answer = gcd__game.gcd__answer()
        if str(rez) == answer:
        #if rez == int(answer):   оригинал
        #if str(c) == answer:
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


