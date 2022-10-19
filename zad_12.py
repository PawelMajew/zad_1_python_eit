#Paweł Majewski EiT Programowanie w języku Python
#zad_12
# Napisz skrypt sumujący dwie macierze o rozmiarach 128x128.
# Wykorzystaj generator liczb losowych do wygenerowania
# macierzy

import random


def random_matrix(size):
    c = [[0] * size for i in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = random.randint(0, 200)

    return c


def sum(matrix_1, matrix_2):
    matrix_sum = [[0]*len(matrix_1) for i in range(len(matrix_1[0]))]
    for i in range(0, len(matrix_1)):
        for j in range(0, len(matrix_1[0])):
            matrix_sum[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return matrix_sum


def print_matrix(temp_matrix):
    for i in range(0, len(temp_matrix)):
        print(temp_matrix[i])


if __name__ == '__main__':
    size = 5
    sum_matrix = [[]]
    matrix = random_matrix(size)
    matrix_1 = random_matrix(size)
    print_matrix(matrix)
    print("===============")
    print_matrix(matrix_1)
    print("===============")
    sum_matrix = sum(matrix, matrix_1)
    print_matrix(sum_matrix)