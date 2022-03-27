import random


class Player:

    def __init__(self, type_player, name=None):
        """
        :param type_player: тип игрока (1 - пользователь или 0 - компьютер)
        :param name: имя игрока
        """
        self.__type_player = type_player
        self.__name = name
        self._len_card = 15
        self._h = 3
        self._w = 9
        self._base_sample = set(random.sample(range(1, 90), self._len_card))
        self._player_card = []  # итоговыя карточка игрока в виде двумерного списка

    @property
    def type_player(self):
        return self.__type_player

    @property
    def name(self):
        return self.__name

    def generate_card(self):
        """
        функция генерации карточки
        :return: карточку игрока в виде списка
        """
        for x in range(self._h):
            inner_list = []
            fill_l = random.sample(range(self._w), 5)
            sample_p = set(random.sample(list(self._base_sample), 5))
            self._base_sample -= sample_p
            sample_p = sorted(sample_p)
            for y in range(self._w):
                if y in fill_l:
                    inner_list.append(str(sample_p.pop(0)).zfill(2))
                else:
                    inner_list.append('  ')
            self._player_card.append(inner_list)

    def show_card(self, type_user):
        """
        :param type_user: тип игрока (1 - пользователь или 0 - компьютер)
        :return:
        """
        show_in_str = '-' * 26 + '\n'
        show_in_str += '{:^26}'.format(self.__name) + '\n'
        show_in_str += '-' * 26 + '\n'
        for i in self._player_card:
            show_in_str += ' '.join(i) + '\n'
        show_in_str += '-' * 26
        return show_in_str

    def update_card(self, number, type_user, mode=None, auto_answer=None):
        """
        Функция принимает число и если оно есть на карте игрока, она зачеркивает его или вызвращает
        0 если пользователь выбрал пропустить
        :param mode: параметр для проверки функции
        :param auto_answer: параметр для проверки функции
        :param number: число
        :param type_user: тип игрока (1 - пользователь или 0 - компьютер)
        :return: 1 - это хорошо и игра продолжается, а return 0 - это плохо, игра завершается
        """
        if type_user == 0:
            for x in range(self._h):
                if str(number).zfill(2) in self._player_card[x]:
                    index = self._player_card[x].index(str(number).zfill(2))
                    self._player_card[x][index] = '--'
                    self._len_card -= 1
                    break
            return 1, self._len_card, self.__name
        else:
            if mode is None:
                answer = input(f'Зачеркнуть цифру для игрока {self.__name}? (y/n): ')
            else:
                answer = auto_answer
            if answer == 'y':
                result = 0
                for x in range(self._h):
                    if str(number).zfill(2) in self._player_card[x]:
                        index = self._player_card[x].index(str(number).zfill(2))
                        self._player_card[x][index] = '--'
                        result = 1
                        self._len_card -= 1
                        break
                return result, self._len_card, self.__name
            elif answer == 'n':
                result = 1
                for x in range(self._h):
                    if str(number).zfill(2) in self._player_card[x]:
                        result = 0
                        break
                return result, self._len_card, self.__name


# Проверка
if __name__ == "__main__":
    player1 = Player(0, 'Comp1')
    player1.generate_card()
    print(player1.show_card(0))
    print(player1.update_card(5, player1.type_player))

    # player1 = Player(1, 'User1')
    # player1.generate_card()
    # print(player1._player_card)
    # tmp_number_in_card = [int(y) for items in player1._player_card for y in items if y.isdigit()][0]
    # print(tmp_number_in_card)
    # print(player1.update_card(tmp_number_in_card, player1.type_player))
