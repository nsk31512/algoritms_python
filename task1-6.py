'''
6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или
равносторонним.
'''

a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    if a != b != c:
        print('Треугольник разносторонний')
    elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
        print('Треугольник равнобедренный')
    elif a == b == c:
        print('Треугольник равносторонний')
else:
    print('Треугольника не существует')

