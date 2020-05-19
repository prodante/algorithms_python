# https://drive.google.com/file/d/1kd3poS7uN1Gj6fOqSg1W9Ncns0luZwSS/view?usp=sharing
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
print('Введите натуральное число (целое и неотрицательное):', end=' ')
number = input('')
even = 0
odd = 0
for num in number:
    if int(num) % 2 == 0:
        even+=1
    else:
        odd+=1
print(f'Количество четных цифр {even}')
print(f'Количество нечетных цифр {odd}')

