class ErrorSetPlayer(Exception):
    def __str__(self):
        return f'Неправильно был задан пользователь'


class ErrorCountPlayers(Exception):
    def __str__(self):
        return f'Неверно ввели кол-во пользователей'


class ErrorChoice(Exception):
    def __str__(self):
        return f'Неверно выбран пункт меню'
