# Программа клиента, запрашивающего текущее время
import argparse
import json
from socket import *
import sys
import time
from common.variables import *


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default='localhost')
    parser.add_argument('-p', '--port', default=str(default_port))

    return parser


def execute_command_presence():
    print('Выполняем команду: `presence`')
    command = {
        'action': 'presence',
        'time': int(time.time()),
        'type': 'status',
        'user': {
            'account_name': account_name,
            'status': 'Yep, I am here!'
        }
    }
    timestamp = int(time.time())
    command['time'] = timestamp
    command['account_name'] = 'Alex'
    result = execute_command(command)

    return result


def connect_to_server(addr, port):
    global sock
    print('Устанавливаем соединение:', (addr, port))
    sock = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    sock.connect((addr, port))  # Соединиться с сервером


def disconnect_from_server():
    print('Отключаемся от сервера', (addr, port))
    sock.close()


def execute_command(msg):
    def parsing_recv(msg):
        respond = json.loads(msg)
        return respond

    msg_send = json.dumps(msg)
    print(msg_send)
    sock.send(msg_send.encode('utf-8'))
    data = sock.recv(block_transfer_size)
    msg_recv = data.decode('utf-8')
    result = parsing_recv(msg_recv)
    print('Сообщение от сервера: {0}; Code: {1}'.format(result['msg'], result['code']))
    return result


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
addr = namespace.addr  # 'localhost'
port = int(namespace.port)
account_name = 'Alex'


connect_to_server(addr=addr, port=port)
execute_command_presence()
disconnect_from_server()
