#Paweł Majewski EiT Programowanie w języku Python
#zad_14
# Napisz skrypt wyliczający wyznacznik macierzy wygenerowanej losowo

import random
def random_matrix(size):
    random_matrix = [[0] * size for i in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            random_matrix[i][j] = random.randint(0, 200)

    return random_matrix


def print_matrix(temp_matrix):
    for i in range(0, len(temp_matrix)):
        print(temp_matrix[i])


def determinant_matrix(matrix, total=0):
    indices = list(range(len(matrix)))

    if len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val

    for iterator in indices:
        temp_matrix = matrix
        temp_matrix = temp_matrix[1:]
        height = len(temp_matrix)

        for i in range(height):
            temp_matrix[i] = temp_matrix[i][0:iterator] + temp_matrix[i][iterator + 1:]

        sign = (-1) ** (iterator % 2)
        temp_det = determinant_matrix(temp_matrix)
        total += sign * matrix[0][iterator] * temp_det

    return total


if __name__ == '__main__':
    size = 5
    matrix = [[]]
    matrix = random_matrix(size)
    print_matrix(matrix)
    print("determinant_matrix: ")
    print(determinant_matrix(matrix))