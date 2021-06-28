'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''

s = 'hello world'
list_of_chars = []
for char in s:
    char_count = s.count(char)
    spam_list = [char, char_count]
    if spam_list not in list_of_chars:
        list_of_chars.append(spam_list)

#for item in list_of_chars:
    #print(item)
dict_coding = {
    'l': '0',
    'o': '10',
    ' ': '110',
    'w': '1110',
    'r': '11110',
    'd': '111110',
    'h': '1111111',
    'e': '1111110'
}

coded_string = ''
for char in s:
    for key, value in dict_coding.items():
        if char == key:
            coded_string += value
            coded_string += ' '

print(coded_string)
