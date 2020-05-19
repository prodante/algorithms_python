# https://drive.google.com/file/d/1kd3poS7uN1Gj6fOqSg1W9Ncns0luZwSS/view?usp=sharing
# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

def sum(i):
    if i == 1:
        return 1
    else:
        return i + sum(i-1)

n = int(input('Введите натуральное число (целое, не отрицательное): '))
# s = 0
# for i in range(1, n + 1):
#     s +=i
s = sum(n)
b = n*(n+1)//2
if s == b:
    print(f'Для множества натуральных чисел равенство 1+2+...+n ({s}) = n(n+1)/2 ({b}) справедливо!')
else:
    print(f'1+2+...+n = {s}')
    print(f'n(n+1)/2 = {b}')
    print(f'Число {n} не является натуральным')
