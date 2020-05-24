# Определить, какое число в массиве встречается чаще всего.
import random

# Функция поиска индекса максимального элемента массива
def search_max(arr):
    max_i = 0
    for i, item in enumerate(arr):
        if item > arr[max_i]:
            max_i = i
    return max_i

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

t = []
a = 0
for i in range(len(array)):
    a = array[i]
    count = 0
    for j in range(len(array)):
        if array[j] == a:
            count += 1
    t.append(count)
index_max = search_max(t)
print(f'Число {array[index_max]} чаще всего ({t[index_max]} раз) встречается в массиве.')