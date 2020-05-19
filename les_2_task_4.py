# https://drive.google.com/file/d/1kd3poS7uN1Gj6fOqSg1W9Ncns0luZwSS/view?usp=sharing
# -*- coding: utf8 -*-
#  Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
n = int(input("Количество элементов ряда: "))
a = 1
i = 0
summa = 0
while i < n:
    summa += a
    a = a/-2
    i += 1
print(f'Сумма элементов ряда {summa}')