import random


class Loto:

    def __init__(self, count_players, player_list):
        self.count_players = count_players
        self.player_list = player_list

    def play(self, show_card=None, mode=None):
        random_n = set(range(1, 91))
        auto_answer = None
        for player in self.player_list:
            player.generate_card()
        while True:
            players = []
            if mode is None:  # если в рабочем режиме, а не тестировании
                look_number = set(random.sample(random_n, 1))
                random_n -= look_number
            else:
                look_number = {100}  # для тестирования
                auto_answer = 'y'
            if show_card is None:
                print(f'Новый  бочонок: {list(look_number)[0]}, (Осталось {len(random_n)})')
                for player in self.player_list:
                    print(player.show_card(player.type_player))

            for player in self.player_list:
                states = player.update_card(list(look_number)[0], player.type_player, mode=mode, auto_answer=auto_answer)
                players.append(states)

            # Далее идут условия окончания игровой партии
            # 1. Игра заканчивается, если хотябы у одного зачеркнуты все цифры
            for player in players:
                _, count_int, name = player
                if count_int == 0:
                    print(f'Поздравляем. У нас есть победитель. Это {name}')
                    return 1

            # 2.  Игра заканчивается, если ...
            # отлавливаются index-ы, чтобы исключить игрока если state = 0
            # записываем индексы всех проигравших
            indices = []
            for index, player in enumerate(players):
                state, count_int, name = player
                if state == 0:
                    print(f'Игрок {name} проигрывает и поэтому выбывает из игры')
                    indices.append(index)
            shift = 0
            for i in indices:
                self.player_list.pop(i - shift)
                shift += 1

            if len(self.player_list) == 1:
                print(f'Остался 1 игрок {self.player_list[0].name}. Победитель!!!')
                return 1
            elif len(self.player_list) == 0:
                print('Важное уведомление!!!')
                print('Все участники игры проиграли, неправильно приняв решение. \nИгра заканчивается')
                return 0
