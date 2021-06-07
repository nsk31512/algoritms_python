'''
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''

matrix = [[0 for _ in range(5)] for _ in range(4)]
print(matrix)

for i in range(len(matrix)):
    summ = 0
    for j in range(len(matrix[i])-1):
        matrix[i][j] = int(input('Введите элемент матрицы: '))
        summ += matrix[i][j]
    matrix[i][4] = summ

for item in matrix:
    for el in item:
        print(f'{el:5}', end='')
    print()
