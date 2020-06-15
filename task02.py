listStr = ['class', 'function', 'method']
for item in listStr:
    bStr = bytes(item, 'utf-8')
    print(bStr, type(bStr), len(bStr))

