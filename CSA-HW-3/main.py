import sys
import time
from container import Container
from extraClasses import inLines

if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) != 5:
        print("Incorrect command line!\n"
              "  Waited:\n"
              "     command -f infile outfile01 outfile02\n"
              "  Or:\n"
              "     command -n number outfile01 outfile02\n")
        exit()
    print('[Start]')
    # Создаём контейнер
    container = Container()
    if sys.argv[1] == "-f":
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        input_file = sys.argv[2]
        try:
            infile = open(input_file)
        except IOError:
            infile = open(input_file, 'w')
        inputLine = infile.read()
        infile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        string_array = inputLine.replace("\n", " ").split(" ")
        amounts = inLines(container, string_array)
        container.print()
        # Открытие потока для записи в первый файл объектов
        outfile = open(sys.argv[3], 'w+')
        container.write(outfile)
        outfile.close()
        print("Source: ",
              round(time.time() - start, 5), " seconds")
        # Открытие потока для записи во второй файл отсортированных объектов
        outfile_sorted = open(sys.argv[4], 'w+')
        container.sort()
        container.write(outfile_sorted)
        outfile_sorted.close()
        # Вывод времени записи
        print("Sorted: ",
              round(time.time() - start, 5), " seconds")
    elif sys.argv[1] == "-n":
        length = int(sys.argv[2])
        # Проверка на размерность
        if length < 1 or length > 10000:
            print("incorrect number of movies = {}. Set 0 < number <= 10000\n", length)
            exit()
        container.staticRndIn(length)
        container.print()
        outfile = open(sys.argv[3], 'w+')
        container.write(outfile)
        outfile.close()
        print("Source: ",
              round(time.time() - start, 5), " seconds")
        outfile_sorted = open(sys.argv[4], 'w+')
        container.sort()
        container.write(outfile_sorted)
        print("Sorted: ",
              round(time.time() - start, 5), " seconds")
        outfile_sorted.close()
    else:
        print("incorrect qualifier value!\n"
              "  Waited:\n"
              "     command -f infile outfile01 outfile02\n"
              "  Or:\n"
              "     command -n number outfile01 outfile02\n");
        exit()
    print('[Finish]')
