# https://drive.google.com/file/d/1kd3poS7uN1Gj6fOqSg1W9Ncns0luZwSS/view?usp=sharing
# -*- coding: utf8 -*- 
# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
import random
answer = random.randint(0, 100)
tryCount = 0
maxTryCount = 10
print(f'Угадайте число от 0 до 100. У Вас {maxTryCount} попыток!')
while True:
    userAnswer = int(input('Введите число от 0 до 100: '))
    tryCount += 1
    if userAnswer == answer:
        print('Поздравляю, вы угадали')
        break
    elif tryCount >= maxTryCount:
        print(f'Вы проиграли. Правильный ответ: {answer}')
        break
    elif userAnswer > answer:
        print(f'Вы ввели слишком большое число, у Вас осталось {maxTryCount - tryCount} попыток.')
    elif userAnswer < answer:
        print(f'Вы ввели слишком маленькое число, у Вас осталось {maxTryCount - tryCount} попыток.')