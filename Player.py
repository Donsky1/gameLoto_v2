import random


class Player:

    def __init__(self, type_player, name=None):
        """
        :param type_player: тип игрока (1 - пользователь или 0 - компьютер)
        :param name: имя игрока
        """
        self.type_player = type_player
        self.len_card = 15
        self.name = name
        self.h = 3
        self.w = 9
        self.base_sample = set(random.sample(range(1, 90), self.len_card))
        self.player_card = []  # итоговыя карточка игрока в виде двумерного списка

    def get_type_player(self):
        return self.type_player

    def generate_card(self):
        """
        функция генерации карточки
        :return: карточку игрока в виде списка
        """
        for x in range(self.h):
            inner_list = []
            fill_l = random.sample(range(self.w), 5)
            sample_p = set(random.sample(list(self.base_sample), 5))
            self.base_sample -= sample_p
            sample_p = sorted(sample_p)
            for y in range(self.w):
                if y in fill_l:
                    inner_list.append(str(sample_p.pop(0)).zfill(2))
                else:
                    inner_list.append('  ')
            self.player_card.append(inner_list)

    def show_card(self, type_user):
        """
        :param type_user: тип игрока (1 - пользователь или 0 - компьютер)
        :return:
        """
        # optional = 'Компьютер' if type_user == 0 else ('Пользователь' if self.name is None else self.name)
        show_in_str = '-' * 26 + '\n'
        show_in_str += '{:^26}'.format(self.name) + '\n'
        show_in_str += '-' * 26 + '\n'
        # temp_player_list = [list(map(str, i)) for i in self.player_list] # перевод каждого элемента в строку
        for i in self.player_card:
            show_in_str += ' '.join(i) + '\n'
        show_in_str += '-' * 26
        print(show_in_str)

    def update_card(self, number, type_user):
        """
        Функция принимает число и если оно есть на карте игрока, она зачеркивает его или вызвращает
        0 если пользователь выбрал пропустить
        :param number: число
        :param type_user: тип игрока (1 - пользователь или 0 - компьютер)
        :return: 1 - это хорошо и игра продолжается, а return 0 - это плохо, игра завершается
        """
        if type_user == 0:
            for x in range(self.h):
                if str(number).zfill(2) in self.player_card[x]:
                    index = self.player_card[x].index(str(number).zfill(2))
                    self.player_card[x][index] = '--'
                    self.len_card -= 1
                    break
            return 1, self.len_card, self.name
        else:
            answer = input(f'Зачеркнуть цифру для игрока {self.name}? (y/n): ')
            if answer == 'y':
                result = 0
                for x in range(self.h):
                    if str(number).zfill(2) in self.player_card[x]:
                        index = self.player_card[x].index(str(number).zfill(2))
                        self.player_card[x][index] = '--'
                        result = 1
                        self.len_card -= 1
                        break
                return result, self.len_card, self.name
            elif answer == 'n':
                result = 1
                for x in range(self.h):
                    if str(number).zfill(2) in self.player_card[x]:
                        result = 0
                        break
                return result, self.len_card, self.name


# Проверка
if __name__ == "__main__":
    player1 = Player(0, 'Comp1')
    player1.generate_card()
    player1.show_card(0)
    print(player1.update_card(5, 0))

    print()
    player1 = Player(1, 'User1')
    player1.generate_card()
    player1.show_card(1)
    print(player1.update_card(56, 1))
