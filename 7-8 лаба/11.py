print('Введите строку')
stroka = input()

if len(stroka) > 10:
    stroka = stroka[:6]
else:
    stroka = stroka.ljust(12, 'o')
print(stroka)
