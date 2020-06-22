# Программа сервера для получения приветствия от клиента и отправки ответа
import argparse
import json
import socket
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default='')
    parser.add_argument('-p', '--port', default='7777')

    return parser


def execute_command_presence(command):
    return 'Команда обработана: {0}'.format(command)


def processing_command(client, addr):
    def parsing_command(msg):
        command = json.loads(msg)
        return command

    def execute_command(command):
        action = command['action']
        if action == 'presence':
            return execute_command_presence(command)
        elif action == '...':
            pass
        else:
            pass

    msg = client.recv(1000000).decode('utf-8')
    print('Сообщение: ', msg, ', принято от клиента: ', addr)
    print('Разбираем запрос: {0}'.format(msg))
    command = parsing_command(msg)
    return execute_command(command)


def sending_responde(client, result):
    print('Возвращаем клиенту {0} ответ: {1}'.format(client.getpeername(), result))
    client.send(result.encode('utf-8'))
    client.close()


def receiver(addr, port):
    s = socket(socket.AF_INET, socket.SOCK_STREAM)  # Создает сокет TCP
    s.bind((addr, port))  # Присваивает порт 8888
    s.listen(5)  # Переходит в режим ожидания запросов;
    # Одновременно обслуживает не более
    # 5 запросов.
    print('Запуск сервера:', (addr, port))
    while True:
        client, addr = s.accept()
        result = processing_command(client, addr)
        sending_responde(client, result)


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
addr = namespace.addr  # 'localhost'
port = int(namespace.port)

receiver(addr, port)
