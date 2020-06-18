"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение
данных в файле YAML-формата.
Для этого:
* Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое
число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
* Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом
обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность
работы с юникодом: allow_unicode = True;
* Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

key1 = ['item1', 'item2', 'item3']
key2 = 50
key3 = {'param1': '1\777', 'param2': '2\777', 'param3': '3\777'}

data_to_yaml = {'key1': key1, 'key2': key2, 'key3': key3}

with open('data.yaml', 'w', encoding="utf-8") as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open('data.yaml', encoding="utf-8") as f_n:
    f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)
print(f_n_content)
