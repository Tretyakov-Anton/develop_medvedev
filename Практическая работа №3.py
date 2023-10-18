import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Генерация случайного массива
my_list = [random.randint(1, 100) for _ in range(10)]

print("Исходный случайный массив:", my_list)
sorted_list = quicksort(my_list)
print("Отсортированный массив:", sorted_list)
