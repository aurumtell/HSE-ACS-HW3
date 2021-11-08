# ----------------------------------------------
import extraClasses
import movies


class Container:
    def __init__(self):
        self.store = []

    def staticRndIn(self, size):
        """
        Добавление случайного объекта в self.store
        :param size: количество объектов
        """
        i = 0
        while i < size:
            self.store.append(extraClasses.inRnd())
            i += 1

    def print(self):
        """
        Вывод информации о контейнере
        """
        print("Container is store", len(self.store), "movies:")
        for movie in self.store:
            movie.print()
        self.sort()
        print("\nSorted container:")
        for movie in self.store:
            movie.print()
        pass

    def write(self, stream):
        """
        Запись информации с контейнера
        :param stream: поток
        """
        stream.write("Container is store {} languages:\n".format(len(self.store)))
        for movie in self.store:
            movie.write(stream)
            stream.write("\n")
        stream.write("\n")
        pass

    def sort(self):
        """
        Сортировка
        """
        for i in range(len(self.store) - 1):
            for j in range(len(self.store) - i - 1):
                if self.store[j].calculation() > self.store[j + 1].calculation():
                    self.store[j], self.store[j + 1] = self.store[j + 1], self.store[j]
