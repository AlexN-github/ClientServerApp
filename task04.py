listStr = ['разработка', 'администрирование', 'protocol', 'standard']
for item in listStr:
    encStr = item.encode('utf-8')
    print(encStr)
    decStr = encStr.decode('utf-8')
    print(decStr)
    print()
