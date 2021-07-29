import random


class GameSettings:
    """
    Method to init game data
    """
    def __init__(self):
        print('Добро пожаловать в игру "Камень, ножницы, бумага"\n'
              'Выберите 1 из инструментов')
        self.user_name: str = 'Имя пользователя'
        self.computer: str = 'Компьютер'
        self.tools: list = ['камень', 'ножницы', 'бумага']
        self.user_choice: str = 'Выбор пользователя'

    def create(self):
        self.user_name = input('Введите имя пользователя: ')
        self.user_choice = input('Выберите 1 из 3 вариантов: ')


class Run:
    @staticmethod
    def run_game():
        game = GameSettings()
        game.create()


Run.run_game()