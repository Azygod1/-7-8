print('Введите строку: ')
s = input()
if len(s) > 5:
    print(s[:3], s[len(s) - 3:])
else:
    print('Строка: ', s[0] * len(s))