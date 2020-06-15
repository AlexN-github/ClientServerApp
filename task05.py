import subprocess


def ping(hostname):
    args = ['ping', hostname]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


listHosts = ['yandex.ru', 'youtube.com']
for item in listHosts:
    ping(item)
