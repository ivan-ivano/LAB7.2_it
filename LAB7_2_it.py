import random


def find_max_element(array, a):
    max_el = array[0]
    for element in array:
        if element > max_el:
            max_el = element
    a.append(max_el)


def find_min_element(array):
    min_el = array[0]
    for element in array:
        if element < min_el:
            min_el = element
    return min_el


def processing_matrix(matrix, a):
    for row in matrix:
        find_max_element(row, a)


def print_matrix(matrix, index=0):
    for row in matrix:
        while index < len(row):
            print(f"{row[index]:>5}{'  ' if index == len(row) - 1 else ''}", end='')
            index += 1
        index = 0
        print()


if __name__ == '__main__':
    max_list = []
    rows, cols = 8, 6
    lower_limit, upper_limit = 16, 97
    matrix = [[random.randint(lower_limit, upper_limit) for _ in range(cols)] for _ in range(rows)]
    print_matrix(matrix)
    processing_matrix(matrix, max_list)
    print("Найменший з максимальних елементів по всіх рядках матриці:", find_min_element(max_list))
