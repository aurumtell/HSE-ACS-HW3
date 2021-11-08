import extraClasses
import random
import movies
import enum


class Legacy(enum.Enum):
    DRAW = 1
    PUPPET = 2
    PLASTICINE = 3


class Cartoon(movies.Movies):
    def __init__(self):
        """
         Инициализация
        :argument self.name: название языка
        :argument self.year: год
        :argument self.legacy: Тип enum
        """
        self.name = ""
        self.year = 0
        self.legacy = Legacy

    def inFile(self, str_array, i):
        """
        Чтение строки
        :param str_array: массив строк
        :param i: количество значений
        :return: int i
        """
        if i >= len(str_array) - 2:
            return 0
        self.name = str_array[i]
        self.year = int(str_array[i + 1])
        self.legacy = Legacy(int(str_array[i + 2]))
        i += 3
        return i

    def inRnd(self):
        """
        Инициализация случайными буквами и цифрами
        """
        self.name = extraClasses.rndString(random.randrange(5, 11))
        self.year = random.randrange(1945, 2021)
        self.legacy = Legacy(random.randrange(1, 4))

    def print(self):
        """
        Вывод информации
        """
        print("Cartoon: name = ", self.name, " year = ", self.year, " legacy = ", self.legacy.name,
              ", calculation = ", round(self.calculation(), 2))
        pass

    def write(self, stream):
        """
        Запись информации в поток
        :param stream: поток
        """
        stream.write(
            "Cartoon: name = {}  year = {}  legacy = {}, calculation = {}".format \
                (self.name, self.year, self.legacy.name, round(self.calculation(), 2)))
        pass

    def calculation(self):
        """
        Вычисление деления int year на длину name
        :return: float result
        """
        return float(self.year) / float(len(self.name))
