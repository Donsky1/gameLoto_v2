from loto import Loto
from player import Player
from errors import ErrorCountPlayers, ErrorChoice, ErrorSetPlayer


def play_game_mode(choice_second, mode=None):
    if choice_second == '1':
        print('\nВы выбрали "компьютер - человек":')
        tmp_player_list = Player.set_players(2, computer=True, pair=False)
        game = Loto(2, tmp_player_list)
        return game.play()
    elif choice_second == '2':
        print('\nВы выбрали "человек - человек":')
        tmp_player_list = Player.set_players(2, computer=False, pair=True)
        game = Loto(2, tmp_player_list)
        return game.play()
    elif choice_second == '3':
        print('\nВы выбрали "компьютер - компьютер":')
        tmp_player_list = Player.set_players(2, computer=True, pair=True)
        game = Loto(2, tmp_player_list)
        return game.play()
    elif choice_second == '4':
        print('\nВы выбрали "Любое кол-во игроков":')
        while True:
            try:
                n_players = input('Введите кол-во игроков: ') if mode is None else mode
                if n_players.isdigit():
                    n_players = int(n_players)
                    tmp_player_list = Player.set_players(n_players)
                    if tmp_player_list != 0:
                        game = Loto(n_players, tmp_player_list)
                        return game.play()
                else:
                    raise ErrorCountPlayers()
            except ErrorSetPlayer as er:
                print(er)
    elif choice_second == '5':
        return exit()
    else:
        raise ErrorChoice()


# запускает игру
if __name__ == '__main__':
    while True:
        try:
            Loto.main_menu()
            choice = input('Выберете пункт меню: ')
            play_game_mode(choice)
        except ErrorCountPlayers as er:
            print(er)
        except ErrorChoice as er:
            print(er)
