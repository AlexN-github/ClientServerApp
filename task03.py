listStr = ['attribute', 'класс', 'функция']
for item in listStr:
    try:
        bStr = item.encode('ascii')
        print(bStr, type(bStr))
    except ValueError:
        print("Oops!  String <<{0}>> not convert bytes type".format(item))
