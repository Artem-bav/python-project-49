def logic_f():
    import random
    signs = "*+-"
    dif_signs = random.choice(signs)
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print(f'a {dif_signs} b') 
    print('PROHOR')
    
def hello_name():
    import prompt
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
    
def question_calc():
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    import random
    import prompt
    answer = 0
    i = 0
    print('What is the result of the expression?')
    signs = "*+-"
    dif_signs = random.choice(signs)
    print(dif_signs)
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if dif_signs == '+':
        c = a + b
    elif dif_signs == '-':
        c = a - b
    else:
        c = a * b
    print(f'c = {c}')
    #rez = a dif_signs b
    #print(f'rez = {rez}')
    print(f'Question: {a} {dif_signs} {b}')
    answer = prompt.string('Your answer: ')
    print(answer)
    
    if c == int(answer):
        print('Correct!')
        i += 1
    else:
        print(f"""Question: {a} {dif_signs} {b}
Your answer: {answer}
'{answer}' is wrong answer ;(. Correct answer was '{c}.
Let's try again, !""")
        i = 4
    print(i)
    dif_signs = ''
    
   
   
   
def hhhhh():   
    
    i = 0
    
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer == 'yes':  # число четное
            print('Correct!')
            answer = ''
            i += 1
        elif number % 2 != 0 and answer == 'no':  # число не четное
            print('Correct!')
            answer = ''
            i += 1
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
    if i == 3:
        print(f'Congratulations, {name}!')
