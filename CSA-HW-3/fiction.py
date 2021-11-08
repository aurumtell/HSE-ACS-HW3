import random
import extraClasses
import movies


class Fiction(movies.Movies):
    def __init__(self):
        """
            Инициализация
            :argument self.name: название языка
            :argument self.year: год
            :argument self.director: название режиссёра
        """
        self.name = ""
        self.year = 0
        self.director = ""

    def inFile(self, lines, count):
        """
            Чтение строки
            :param lines: массив строк
            :param count: количество значений
            :return: int amount
        """
        if count >= len(lines) - 2:
            return 0
        self.name = lines[count]
        self.year = int(lines[count + 1])
        self.director = lines[count + 2]
        count += 3
        return count

    def inRnd(self):
        """
        Инициализация случайными буквами и цифрами
        """
        self.name = extraClasses.rndString(random.randrange(5, 11))
        self.year = random.randrange(1945, 2021)
        self.director = extraClasses.rndString(random.randrange(5, 11))

    def print(self):
        """
        Вывод информации
        """
        print("Fiction: name = ", self.name, " year = ", self.year, " director = ", self.director,
              ", quotient = ",
              round(self.calculation(), 2))
        pass

    def write(self, stream):
        """
        Запись информации в поток
        :param stream: поток
        """
        stream.write(
            "Fiction: name = {}  year = {}  director = {} , quotient = {}".format \
                (self.name, self.year, self.director,
                 round(self.calculation(), 2)))
        pass

    def calculation(self):
        """
        Вычисление деления int year на длину name
        :return: float result
        """
        return float(self.year) / float(len(self.name))
