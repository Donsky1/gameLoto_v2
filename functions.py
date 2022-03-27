from Player import Player


def main_menu():
    print('-'*30)
    print('Режим игры')
    print('1. компьютер - человек')
    print('2. человек - человек')
    print('3. компьютер - компьютер')
    print('4. Любое кол-во игроков')
    print('5. Выход из игры')


def set_players(count, computer=True, pair=False):
    # Player(0/1): 0 - comp, 1 - user
    # count - кол-во игроков
    player_list = []
    if count == 2:
        if computer == True and pair == False:
            player_list = [Player(0, name='Comp1'), Player(1, name='User1')]
        elif computer == True and pair == True:
            player_list = [Player(0, name='Comp1'), Player(0, name='Comp2')]
        elif computer == False and pair == True:
            player_list = [Player(1, name='User1'), Player(1, name='User2')]
    elif count > 2:
        print('-'*100)
        print('Используя следующий формат введите игрока: [0/1],[name]')
        print('Используйте символ разделения запятую. 0 - Бот, 1 - Пользователь')
        print('Пример1: 0,Comp1 - Это значит бот с именем Comp1')
        print('Пример2: 1,Masha - Это значит человек с именем Masha')
        print('-' * 100)
        try:
            for i in range(count):
                player = input(f'Игрок {i+1}. Введите: ').split(',')
                player_list.append(Player(int(player[0]), name=player[1]))
        except Exception as er:
            print(f'произошла ошибка: {er}')
            return 0
    return player_list


if __name__ == "__main__":
    player_list = set_players(2, computer=True, pair=False)
    for player in player_list:
        player.generate_card()
    for player in player_list:
        player.show_card(player.get_type_player())