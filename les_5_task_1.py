""" Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего. """
from collections import defaultdict, deque

comp = defaultdict(list)
kol_companies = int(input('Введите количество предприятий: '))
total_profit = 0
for i in range(kol_companies):
    name_comp = input(f'Как назовем {i+1} предприятие: ')
    for j in range(4):
        profit_comp = int(input(f'Прибыль за {j+1}-й квартал: '))
        comp[name_comp].append(profit_comp)
        total_profit += profit_comp
#print(comp)
average_profit = total_profit // kol_companies
d_higher = deque()
d_below = deque()
for i in comp:
    if average_profit < sum(comp[i]):
        d_higher.append(i)
    else:
        d_below.append(i)
print('+'*40)
print(f'Средняя прибыль предприятий: {average_profit}\nПредприятия с доходом выше среднего: {", ".join(d_higher)}\nПредприятия с доходом ниже среднего: {", ".join(d_below)}')