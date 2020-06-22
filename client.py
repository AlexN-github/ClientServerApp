# Программа клиента, запрашивающего текущее время
import argparse
import json
import socket
import sys
import time


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr')
    parser.add_argument('-p', '--port', default='7777')

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
    execute_command(command)

    return command


def connect_to_server(addr, port):
    global sock
    print('Устанавливаем соединение:', (addr, port))
    sock = socket(socket.AF_INET, socket.SOCK_STREAM)  # Создать сокет TCP
    sock.connect((addr, port))  # Соединиться с сервером


def disconnect_from_server():
    print('Отключаемся от сервера', (addr, port))
    sock.close()


def execute_command(command):
    msg_send = json.dumps(command)
    print(msg_send)
    sock.send(msg_send.encode('utf-8'))
    data = sock.recv(1000000)
    msg_recv = data.decode('utf-8')
    print('Сообщение от сервера: ', msg_recv, ', длиной ', len(msg_recv), ' байт')
    return msg_recv


parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
addr = namespace.addr  # 'localhost'
port = int(namespace.port)
account_name = 'Alex'


connect_to_server(addr=addr, port=port)
execute_command_presence()
disconnect_from_server()
