# Программа сервера для получения приветствия от клиента и отправки ответа
import argparse
import json
from socket import *
import sys
from common.variables import *


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default=str(server_addr_default))
    parser.add_argument('-p', '--port', default=str(default_port))

    return parser


def execute_command_presence(command):
    result = {}
    result['msg'] = 'command `{0}` completed successfully'.format(command['action'])
    result['code'] = 200
    return result


def processing_command(client, addr):
    def parsing_command(msg):
        command = json.loads(msg)
        return command

    def execute_command(command):
        action = command['action']
        if action == 'presence':
            result = execute_command_presence(command)
        elif action == '...':
            pass
        else:
            result = {}
            result['msg'] = 'Invalid command'
            result['code'] = 400
        return result

    msg = client.recv(block_transfer_size).decode('utf-8')
    print('Сообщение: ', msg, ', принято от клиента: ', addr)
    print('Разбираем запрос: {0}'.format(msg))
    command = parsing_command(msg)
    return execute_command(command)


def sending_responde(client, result):
    print('Возвращаем клиенту {0} msg: {1}; code: {2}'.format(client.getpeername(), result['msg'], result['code']))
    msg_send = json.dumps(result)
    client.send(msg_send.encode('utf-8'))
    client.close()


def receiver(addr, port):
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    s.bind((addr, port))  # Присваивает порт 8888
    s.listen(5)  # Переходит в режим ожидания запросов;
    # Одновременно обслуживает не более
    # 5 запросов.
    print('Запуск сервера:', (addr, port))
    while True:
        client, addr = s.accept()
        try:
            result = processing_command(client, addr)
            sending_responde(client, result)
        except Exception:
            result = {}
            result['msg'] = 'Unexpected error'
            result['code'] = 500
            sending_responde(client, result)



parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
addr = namespace.addr  # 'localhost'
port = int(namespace.port)

receiver(addr, port)
