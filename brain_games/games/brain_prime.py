import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def number_prime_test(number):
    if number == 2 or number == 3 or number == 5 or number == 7:
        return True
    if number % 2 == 0 and number != 2:
        #print('A')
        return False
    for i in range(3, int(number / 2), 2):
        #print('i')
        if number % i == 0:
            return False
            #answer = False
            #print('answer')
            #break
        #else:
        #    print('C')
         #   answer = True
    #print('F')
    return True

def ask_answer():
    number = random.randint(2, 1000)  # случайное число
    ask = str(number)
    if number_prime_test(number) is True:
        #print('kkkkk')
        answer = 'yes'
    else:
        print('L')
        answer = 'no'
    return ask, str(answer)
