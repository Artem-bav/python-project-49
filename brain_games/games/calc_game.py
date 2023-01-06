def calc_user():

    from brain_games import logic_game
    name = logic_game.hello_name() # переменная name получает знач из RETURNA функц
    counter_i = 0 
    while counter_i <= 2:
        
        i = logic_game.question_calc() # выполнил функц и присвоил
# переменной i =  return i   результ выполнения функц
        counter_i += i
        if counter_i == 3:
            print(f'Congratulations, {name}!')

