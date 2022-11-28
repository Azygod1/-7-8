s = str(input())
v = 0
x = 0
c = 0
while x <= len(s):
    if s[x] == 'x':
        c = 0
        print('x')
    if s[x] == 'w':
        s = 0
        print('w')
    else:
        c += 1
    x += 1
if c >= 1:
    print('нет такого')
