# https://drive.google.com/file/d/1LzNxHnLB9E5LRezVn7yJV25z5Mm-77i-/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = int(input("Введите трехзначное число: "))
n1 = number // 100
print(f'{n1 = }')
n2 = number % 100 // 10
print(f'{n2 = }')
n3 = number % 10
print(f'{n3 = }')
amount = n1 + n2 + n3
comp = n1 * n2 * n3
print(f'Сумма цифр числа: {amount}')
print(f'Произведение цифр числа: {comp}')