import csv
from math import sqrt
import time
import matplotlib.pyplot as plt


min_value = [100, 0, 0]
max_value = [0, 0, 0]
step = 0
distance_distribution_dict = {}
while step < 15:
    distance_distribution_dict[round(step, 1)] = 0
    step += 0.1


def distance(row_one, row_two, line_start, line_end):
    """ Функция вычисления минимального и максимального расстояния """

    global max_value, min_value, distance_distribution_dict
    count = [pow(float(x)-float(y), 2) for x, y in zip(row_one, row_two)]
    count = sqrt(sum(count))

    if count >= max_value[0]:
        max_value = [count, line_start, line_end]
    if count <= min_value[0]:
        min_value = [count, line_start, line_end]
    distance_distribution_dict[round(count, 1)] += 1


def preparation_of_lists(vectors):
    """ Функция для подготовки векторов """

    number_of_lines = len(vectors)
    line_end = number_of_lines
    line_start = 0

    while line_start < (line_end - 1):
        while line_end > (line_start + 1):
            distance(vectors[line_start],
                     vectors[line_end-1],
                     line_start+1,
                     line_end)
            line_end -= 1
        line_end = number_of_lines
        line_start += 1


def main():
    """ Функция для чтения csv файла """

    vectors = []
    with open('vectors.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            vectors.append(row)
    preparation_of_lists(vectors)

    print('Евклидово расстояние между всеми парами различных векторов '
          f'списка:\n- минимальное значение равно {min_value[0]} для '
          f'строк {min_value[1]} и {min_value[2]}.\n- максимальное '
          f'значение равно {max_value[0]} для строк {max_value[1]} '
          f'и {max_value[2]}.\n')


def distance_distribution():
    """ Функция построения графика """

    index_start = 0
    index_end = -1
    list_y = list(distance_distribution_dict.values())
    list_x = list(distance_distribution_dict.keys())
    while list_y[index_start] == 0:
        index_start += 1
    while list_y[index_end] == 0:
        index_end -= 1

    plt.bar(list_x[index_start:index_end],
            list_y[index_start:index_end],
            color='g',
            width=0.085)
    plt.grid(True)


if __name__ == '__main__':
    start_time = time.time()

    main()
    distance_distribution()

    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()
