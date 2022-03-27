from player import Player


def main_menu():
    print('-' * 30)
    print('Режим игры')
    print('1. компьютер - человек')
    print('2. человек - человек')
    print('3. компьютер - компьютер')
    print('4. Любое кол-во игроков')
    print('5. Выход из игры')


def set_list_players(count, mode=None):
    """
    mode - режим тестирования функцмй
    """
    player_list = []
    if count > 2:
        try:
            for i in range(count):
                tmp_player = input(f'Игрок {i + 1}. Введите: ').split(',') if mode is None else '0,TEST'
                player_list.append(Player(int(tmp_player[0]), name=tmp_player[1]))
        except Exception as er:
            print(f'произошла ошибка: {er}')
            return 0
    return player_list


def set_players(count, computer=True, pair=False, mode=None):
    """
    mode - режим тестирования функцмй
    Player(0/1): 0 - comp, 1 - user
    count - кол-во игроков
    """
    if count == 2:
        if computer is True and pair is False:
            player_list = [Player(0, name='Comp1'), Player(1, name='User1')]
        elif computer is True and pair is True:
            player_list = [Player(0, name='Comp1'), Player(0, name='Comp2')]
        elif computer is False and pair is True:
            player_list = [Player(1, name='User1'), Player(1, name='User2')]
        else:
            return 0
    elif count > 2:
        if mode is None:
            print('-' * 100)
            print('Используя следующий формат введите игрока: [0/1],[name]')
            print('Используйте символ разделения запятую. 0 - Бот, 1 - Пользователь')
            print('Пример1: 0,Comp1 - Это значит бот с именем Comp1')
            print('Пример2: 1,Masha - Это значит человек с именем Masha')
            print('-' * 100)
        return set_list_players(count, mode=mode)
    else:
        return 0
    return player_list


if __name__ == "__main__":
    player_list = set_players(2, computer=True, pair=False)
    for player in player_list:
        player.generate_card()
    for player in player_list:
        player.show_card(player.get_type_player())
