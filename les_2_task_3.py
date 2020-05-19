# https://drive.google.com/file/d/1kd3poS7uN1Gj6fOqSg1W9Ncns0luZwSS/view?usp=sharing
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# рекурсивная фнкция
# def rec(n,i):
#     return i if (n==0) else rec(n//10, i*10 + n%10)

number1 = int(input("Введите целое число: "))
number2 = 0
while number1 > 0:
	digit = number1 % 10 	  # находим остаток - последнюю цифру числа
	number1 = number1 // 10   # делим нацело - убираем из числа последнюю цифру
	number2 = number2 * 10    # увеличиваем разрядность второго числа
	number2 = number2 + digit # добавляем очередную цифру
print('"Обратное" ему число:',number2)

#result = rec(number1, 0) 
#print(result)