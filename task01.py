"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:
* Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных
выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться
четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
«Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл
main_data (также для каждого файла);
* Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции
реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных
данных в соответствующий CSV-файл;
* Проверить работу программы через вызов функции write_to_csv().
"""
import csv

def get_data():
    list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    lists = [
        {
            'name_list': 'os_prod_list',
            'name_prop': 'Изготовитель системы',
            'list_': []
        },
        {
            'name_list': 'os_name_list',
            'name_prop': 'Название ОС',
            'list_': []
        },
        {
            'name_list': 'os_code_list',
            'name_prop': 'Код продукта',
            'list_': []
        },
        {
            'name_list': 'os_type_list',
            'name_prop': 'Тип системы',
            'list_': []
        },
    ]
    for f in list_files:
        with open(f) as f_n:
            file_content = f_n.read()
            for row in file_content.split('\n'):
                for item in lists:
                    if item['name_prop'] in row:
                        val = row.replace(item['name_prop'] + ':', "").strip()
                        item['list_'].append(val)
    return lists


def write_to_csv(rep_file_name):
    lists = get_data()
    with open(rep_file_name, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        row_header = []
        for item in lists:
            row_header.append(item['name_prop'])
        f_n_writer.writerow(row_header)
        for i in range(len(lists[0]['list_'])):
            row = []
            for item in lists:
                row.append(item['list_'][i])
            f_n_writer.writerow(row)


write_to_csv('report.csv')
