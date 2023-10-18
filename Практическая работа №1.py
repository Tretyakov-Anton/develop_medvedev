while True:
    try:
        n = int(input("Введите основание равнобедренного треугольника, число должно быть нечетным: "))
        if n < 0 or n % 2 == 0:
            raise ValueError
        break
    except ValueError:
        print("Некорректный ввод. Размер фигуры должен быть неотрицательным и нечетным числом.")

base = n
height = n // 2 + 1

for i in range(base):
    for j in range(height):
        if j == 0 or i == base + 1 or i == j or i == base - 1 - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
 
