import csv
import random


def main():
    """ Функция для создания csv файла """

    n, m = [None, None]
    while n is None:
        try:
            n = int(input('Введите количество строк 500 < N ≤ 1000: '))
            while n <= 500 or n > 1000:
                if n <= 500:
                    print('Вы ввели неверное число, '
                          f'указанное число {n} ≤ 500')
                if n > 1000:
                    print('Вы ввели неверное число, '
                          f'указанное число {n} > 1000')
                n = int(input('Введите количество строк 500 < N ≤ 1000: '))
        except ValueError:
            print('Введите целое число!')
            n = None

    while m is None:
        try:
            m = int(input('Введите количество столбцов 10 < m ≤ 50: '))
            while m <= 10 or m > 50:
                if m <= 10:
                    print(f'Вы ввели неверное число, указанное число {m} ≤ 10')
                if m > 50:
                    print(f'Вы ввели неверное число, указанное число {m} > 50')
                m = int(input('Введите количество столбцов 10 < m ≤ 50: '))
        except ValueError:
            print('Введите целое число!')
            m = None

    with open('vectors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(n):
            writer.writerow([random.uniform(-1, 1) for _ in range(m)])


if __name__ == '__main__':
    main()
