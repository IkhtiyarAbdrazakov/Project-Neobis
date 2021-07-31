import random


print('Добро пожаловать в игру "Камень, ножницы, бумага"')


class GameSettings:
    user_name: str = input('Введите свое имя: ')
    """
    Method initializes game data
    """
    def __init__(self):
        self.tools: list = ['камень', 'ножницы', 'бумага']
        self.user_choice: str = 'Выбор пользователя'
        self.computer_choice: str = 'Выбор компьютера'
        self.continue_choice: str = 'Выбор продолжения игры'


class GameLogic(GameSettings):
    def main_logic(self):
        """
        Method controls the main logic of the game
        :return: Game round result
        """
        self.user_choice = input(f'{self.user_name} cделайте выбор — камень, ножницы или бумага: ').lower()
        self.computer_choice = random.choice(self.tools)
        if self.user_choice == self.computer_choice:
            return f'Оба игрока выбрали {self.user_choice}. Ничья!'
        elif self.user_choice == self.tools[0] and self.computer_choice == self.tools[1] or \
                self.user_choice == self.tools[1] and self.computer_choice == self.tools[2] or \
                self.user_choice == self.tools[2] and self.computer_choice == self.tools[0]:
            return f'{self.user_name} выбрал(a) "{self.user_choice}", ' \
                   f'компьютер выбрал "{self.computer_choice}". Вы победили!'
        else:
            return f'{self.user_name} выбрал(a) "{self.user_choice}", ' \
                   f'компьютер выбрал "{self.computer_choice}". Вы проиграли!'

    def continue_game(self):
        """
        Methode gives choice to continue game or not
        :return:
        """
        self.continue_choice = input(f'{self.user_name}, вы хотите продолжить игру?(да/нет): ').lower()
        if self.continue_choice == 'да':
            return self.main_logic(), self.continue_game()
        else:
            print('Спасибо за игру!')


class Run:
    @staticmethod
    def run_game():
        """
        Methode runs the game
        :return:
        """
        game_settings = GameSettings()
        game_settings.__init__()
        game_logic = GameLogic()
        print(game_logic.main_logic())
        game_logic.continue_game()


Run().run_game()
