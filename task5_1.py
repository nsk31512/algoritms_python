'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple

Company = namedtuple('Company', ['name', 'profit'])

n = int(input('Введите количество компаний: '))

companies = list()

for i in range(n):
    name_profit = input('Введите название комании и прибыль через пробел: ').split()
    name_profit[1] = float(name_profit[1])
    new_company = Company._make(name_profit)
    companies.append(new_company)

summator = 0
for item in companies:
    summator += item[1]
avrg_prof = summator / n

cmpns_below_avrg = []
cmpns_above_avrg = []
for item in companies:
    if item[1] > avrg_prof:
        cmpns_above_avrg.append(item[0])
    else:
        cmpns_below_avrg.append(item[0])
print(f'Средняя прибыль среди всех компаний {avrg_prof}')
print('Компании с прибылью больше средней: ', end='')
for item in cmpns_above_avrg:
    print(item, end=', ')
print()
print('Компании с прибылью меньше средней: ', end='')
for item in cmpns_below_avrg:
    print(item, end=', ')
print()
