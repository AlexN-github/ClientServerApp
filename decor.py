import inspect
import io
from datetime import datetime


def log(func):
    def wrapper(*args, **kwargs):
        print('Выполняется функция декоратор')
        f = io.open('log.txt', mode='w', encoding='utf-8')
        parent_func = inspect.stack()[1][3]
        msg = '{0} Функция `{1}` вызвана из функции `{2}`'.format(datetime.now().strftime('%d/%m/%Y %H:%M:%S'), func.__name__, parent_func)
        print(msg)
        f.write(msg)
        print('Запускаем основную функцию')
        res = func(*args, **kwargs)
        print(res)
    return wrapper


@log
def func_z():
    return 'Основная функция выполнена'


def main():
    func_z()


main()
