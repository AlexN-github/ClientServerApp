listStr = ['сетевое программирование', 'сокет', 'декоратор']
filename = 'c:/test_file.txt'

f_n = open(filename, "w")
[f_n.write(item+'\r') for item in listStr]
f_n.close()

with open(filename) as f_n:
    print('Encoding: '+f_n.encoding)

with open(filename, encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
