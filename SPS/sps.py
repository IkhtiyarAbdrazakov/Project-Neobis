class ResultWrite:
    def file_write(self, result):
        """
        A method that records the progress of the game to a file and outputs it to the console
        :param result:
        :return:
        """
        with open('result.txt', 'a', encoding='utf-8 ') as f:
            f.write(f'{result} \n')

        with open('result.txt', 'r', encoding='utf-8') as file:
            print(file.read())


