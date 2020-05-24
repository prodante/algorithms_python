# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
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
MIN_ITEM = 10
MAX_ITEM = 25
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
index_max = search_max(array)
index_min = search_min(array)
print(f'Минимальный элемент массива: {array[index_min]}')
print(f'Максимальный элемент массива: {array[index_max]}')
sum_element = 0
if index_min > index_max:
    temp_var = index_min
    index_min = index_max
    index_max = temp_var 
for j in range(index_min + 1, index_max):
        sum_element += array[j]
print(f'Сумму элементов, находящихся между минимальным и максимальным элементами = {sum_element}')  