import random

while True:
    try:
        n = int(input("Введите количество строк в матрице (1 < n <= 100): "))
        m = int(input("Введите количество столбцов в матрице (1 < m <= 50): "))
        if 1 < n <= 100 and 1 < m <= 50:
            break
        else:
            raise ValueError
    except ValueError:
        print("Неправильный ввод. Повторите попытку.")

def sortmatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(1, n):
        key = matrix[i][0]
        j = i - 1

        while j >= 0 and matrix[j][0] > key:
            matrix[j + 1], matrix[j] = matrix[j], matrix[j + 1]
            j -= 1

    return matrix

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        element = random.randint(1, 100)
        row.append(element)
    matrix.append(row)

initial_matrix = [row[:] for row in matrix]

sortedmatrix = sortmatrix(matrix)

print("Исходная матрица:")
for row in initial_matrix:
    print(row)

print("Упорядоченная матрица:")
for row in sortedmatrix:
    print(row)
