print('Введите строки')
stroka1 = input()
stroka2 = input()

с = abs(len(stroka1) - len(stroka2))

if len(stroka1) > len(stroka2):
    print(stroka1 * с)
else:
    print(stroka2 * с)
