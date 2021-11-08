import random
import extraClasses
import movies


class Documentary(movies.Movies):
    def __init__(self):
        """
            Инициализация
            :argument self.name: название языка
            :argument self.year: год
            :argument self.duration: длительность
        """
        self.name = ""
        self.year = 0
        self.duration = 0

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
        self.duration = int(lines[count + 2])
        count += 3
        return count

    def inRnd(self):
        """
        Инициализация случайными буквами и цифрами
        """
        self.name = extraClasses.rndString(random.randrange(5, 11))
        self.year = random.randrange(1945, 2021)
        self.duration = random.randrange(5, 100)

    def print(self):
        """
        Вывод информации
        """
        print("Documentary: name = ", self.name, " year = ", self.year, " duration = ", self.duration,
              ", calculation = ",
              round(self.calculation(), 2))
        pass

    def write(self, stream):
        """
        Запись информации в поток
        :param stream: поток
        """
        stream.write(
            "Documentary: name = {}  year = {}  duration = {} , calculation = {}".format \
                (self.name, self.year, self.duration,
                 round(self.calculation(), 2)))
        pass

    def calculation(self):
        """
        Вычисление деления int year на длину name
        :return: float result
        """
        return float(self.year) / float(len(self.name))
