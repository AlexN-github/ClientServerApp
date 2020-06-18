"""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.
Для этого:
* Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна
предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
* Проверить работу программы через вызов функции write_order_to_json() с передачей в нее
значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json') as f_n:
        objs = json.load(f_n)
    print(objs['orders'])
    objs['orders'].append(order)
    print(objs)

    with open('orders.json', 'w') as f_n:
        json.dump(objs, f_n, indent=4)


write_order_to_json(item='pupet2', quantity=1, price=100, buyer='Petrov Ivan Ivanovich', date='01.01.2020')
