print('Введите строку: ')
stroka = input()
print('Кол-во + и - после которых стоит 0:', stroka.count('-0') + stroka.count('+0'))
print('Кол-во + и -:', stroka.count('-') + stroka.count('+'))
