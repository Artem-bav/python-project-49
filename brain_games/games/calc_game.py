def calc_user():
    #from brain_games.games.logic_game import logic_f #вызов логики
    #name = '' # объявили глобально
    from brain_games import logic_game
    name = logic_game.hello_name() # переменная name получает значение из RETURNA функц
    #logic_game.question_calc()
    answer, i = logic_game.question_calc() #присвоил переменным 
    # answer = answer  i = i return результата выполнения функц
    
    
    print(answer)
    print(answer)
    print(answer)
    print(i)
    print(i)
    print(name) # это локальная name, а не глобальная
    print('artem kozel')
