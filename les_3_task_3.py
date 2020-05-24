# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

# Функция поиска индекса максимального элемента массива
def search_max(arr):
    max_i = 0
    for i, item in enumerate(arr):
        if item > arr[max_i]:
            max_i = i
    return max_i

# Функция поиска индекса минимального элемента массива
def search_min(arr):
    min_i = 0
    for i, item in enumerate(arr):
        if item < arr[min_i]:
            min_i = i
    return min_i

SIZE = 10
MIN_ITEM = 22
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

############### 1 вариант с использованием функций ###############
# max_ = search_max(array)
# min_ = search_min(array)

############### 2 вариант ###############
max_ = min_ = 0
for i in range(1, len(array)):
    if array[i] > array[max_]:
        max_ = i
    elif array[i] < array[min_]:
        min_ = i 

print(f'Индекс максимального элемента массива: {max_}')
print(f'Индекс минимального элемента массива: {min_}')
# меняем местами минимальный и максимальный элементы
x = array[max_]
array[max_] = array[min_]
array[min_] = x
print(f'Результирующий массив: {array}')