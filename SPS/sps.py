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
        self.result: str = 'Результат игры'


class GameLogic(GameSettings):
    def main_logic(self):
        """
        Method controls the main logic of the game
        :return: Game round result
        """
        self.user_choice = input(f'{self.user_name} cделайте выбор — камень, ножницы или бумага: ').lower()
        self.computer_choice = random.choice(self.tools)
        if self.user_choice == self.computer_choice:
            self.result = f'Оба игрока выбрали {self.user_choice}. Ничья!'
            return self.result
        elif self.user_choice == self.tools[0] and self.computer_choice == self.tools[1] or \
                self.user_choice == self.tools[1] and self.computer_choice == self.tools[2] or \
                self.user_choice == self.tools[2] and self.computer_choice == self.tools[0]:
            self.result = f'{self.user_name} выбрал(a) "{self.user_choice}", ' \
                          f'компьютер выбрал "{self.computer_choice}". Победил {self.user_name}!'
            return self.result
        else:
            self.result = f'{self.user_name} выбрал(a) "{self.user_choice}", ' \
                          f'компьютер выбрал "{self.computer_choice}". Победил компьютер!'
            return self.result

    # def continue_game(self):
    #     """
    #     Methode gives choice to continue game or not
    #     :return:
    #     """
    #     self.continue_choice = input(f'{self.user_name}, вы хотите продолжить игру?(да/нет): ').lower()
    #     if self.continue_choice == 'да':
    # #         return self.main_logic(), self.continue_game()
    #     else:
    #         print('Спасибо за игру!')


class ResultWrite:
    @staticmethod
    def file_write(result):
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(f'{result}\n')


class Run:
    @staticmethod
    def run_game():
        """
        Methode runs the game
        :return:
        """
        while True:
            game_settings = GameSettings()
            game_logic = GameLogic()
            game_settings.result = game_logic.main_logic()
            print(game_settings.result)
            result_write = ResultWrite()
            result_write.file_write(game_settings.result)
            continue_choice = input('Вы хотите продолжить игру?(да/нет): ').lower()
            if continue_choice == 'да':
                return Run().run_game()
            else:
                print('Спасибо за игру!')
                break


Run().run_game()
