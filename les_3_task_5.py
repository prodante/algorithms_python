# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

# Функция поиска индекса максимального отрицательного элемента массива
def search_max(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            max_i = i   # первый отрицательный элемент в массиве
            break
    for i, item in enumerate(arr):
        if item < 0:
            if item > arr[max_i]:
                max_i = i
    return max_i

SIZE = 20
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
index_max = search_max(array)
print(f'Максимальный отрицательный элемент массива\nпозиция: {index_max}, значение: {array[index_max]}')