'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
'''


def freq_rate(my_list, div):
    count = 0
    for item in my_list:
        if item % div == 0:
            count += 1
    return count


new_list = [el for el in range(2, 100)]
div_list = [el for el in range(2,10)]
for item in div_list:
    print(f'{freq_rate(new_list, item)} чисел кратны {item}')
