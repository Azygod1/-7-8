s = input()

if s[:3] == 'abc':
    s = 'www' + s[3:]
else:
    s += 'zzz'

print(s)
