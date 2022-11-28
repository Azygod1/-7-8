text = input('Введите строку: ')
text = text.lower()
text = list(str(text))
last_symbol = len(text) - 1
i = 0

while i < last_symbol:
    if text[i] == text[last_symbol]:
        print(i)
    i += 1
