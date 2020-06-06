# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы
import random
""" Переменная spam служит некоторым флагом контроля перестановок в массиве. Если на очередной
    итерации "пузерей" ))) не оказалось, то массив отсортирован. """
def bubble_sort(arr):
    n = 1
    while n < len(arr):
        spam = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                spam += 1
        if spam == 0:
            break
        n += 1
    return arr

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
print(f'Отсортированный массив: {bubble_sort(array)}')