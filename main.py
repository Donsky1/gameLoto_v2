from loto import Loto
from functions import *


def play_game_mode(choice_second):
    if choice_second == '1':
        print('Вы выбрали "компьютер - человек":')
        player_list = set_players(2, computer=True, pair=False)
        game = Loto(2, player_list)
        game.play()
    elif choice_second == '2':
        print('Вы выбрали "человек - человек":')
        player_list = set_players(2, computer=False, pair=True)
        game = Loto(2, player_list)
        game.play()
    elif choice_second == '3':
        print('Вы выбрали "компьютер - компьютер":')
        player_list = set_players(2, computer=True, pair=True)
        game = Loto(2, player_list)
        game.play()
    elif choice_second == '4':
        print('Вы выбрали "Любое кол-во игроков":')
        try:
            n_players = int(input('Введите кол-во игроков: '))
            player_list = set_players(n_players)
            if player_list != 0:
                game = Loto(n_players, player_list)
                game.play()
        except Exception as er:
            print(f'произошла ошибка: {er}')
    elif choice_second == '5':
        exit()
    else:
        print('Неверный пункт меню')


# запускает игру
while True:
    main_menu()
    choice = input('Выберете пункт меню: ')
    play_game_mode(choice)
