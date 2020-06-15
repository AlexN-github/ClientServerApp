listStr = ['разработка', 'сокет', 'декоратор']
for item in listStr:
    print(item, type(item))

listStr2 = [
    {'разработка': b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'},
    {'сокет': b'\u0441\u043e\u043a\u0435\u0442'},
    {'декоратор': b'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'}
]

for item in listStr2:
    print(item, type(item))
