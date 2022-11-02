#Paweł Majewski EiT Programowanie w języku Python
#zad_13
# Napisz skrypt realizujący mnożenie dwóch macierzy o rozmiarach 8x8
import random


def random_matrix(size):
    random_matrix = [[0] * size for i in range(size)]

    for i in range(0, size):
        for j in range(0, size):
            random_matrix[i][j] = random.randint(0, 200)

    return random_matrix


def multiplication(matrix_1, matrix_2):
    matrix_multiplication = [[0]*len(matrix_1) for i in range(len(matrix_1[0]))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1)):
            for k in range(len(matrix_1)):
                matrix_multiplication[i][j] = matrix_multiplication[i][j] + matrix_1[i][k] * matrix_2[k][j]
    return matrix_multiplication


def print_matrix(temp_matrix):
    for i in range(0, len(temp_matrix)):
        print(temp_matrix[i])


if __name__ == '__main__':
    size = 8
    multiplication_matrix = [[]]
    matrix = random_matrix(size)
    matrix_1 = random_matrix(size)
    print_matrix(matrix)
    print("===============")
    print_matrix(matrix_1)
    print("===============")
    multiplication_matrix = multiplication(matrix, matrix_1)
    print_matrix(multiplication_matrix)



