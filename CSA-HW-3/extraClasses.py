import random
import string

from cartoon import Cartoon
from documentary import Documentary
from fiction import Fiction


def inLines(container, string_line):
    """
    :param container: Contains objects
    :param string_line: Input
    :return: string
    """
    array_len = len(string_line)
    i = 0  # Индекс, задающий текущую строку в массиве
    amount = 0
    while i < array_len:
        line = string_line[i]
        key = int(line)
        if key == 1:
            i += 1
            movie = Fiction()
            i = movie.inFile(string_line, i)
        elif key == 2:
            i += 1
            movie = Cartoon()
            i = movie.inFile(string_line, i)
        elif key == 3:
            i += 1
            movie = Documentary()
            i = movie.inFile(string_line, i)
        else:
            return amount
        if i == 0:
            return amount
        amount += 1
        container.store.append(movie)
    return amount


def inRnd():
    """
    Выбор случайного сгенерированного объекта
    :return: Объект базового класса Movie
    """
    key = random.randrange(1, 4)
    if key == 1:
        movie = Fiction()
        movie.inRnd()
        return movie
    elif key == 2:
        movie = Cartoon()
        movie.inRnd()
        return movie
    else:
        movie = Documentary()
        movie.inRnd()
        return movie


def rndString(length_str):
    """
    Рандомизация случайных букв
    :param length_str: длина строки
    :return: случайная строка
    """
    letters = string.ascii_uppercase + string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length_str))
    return result
