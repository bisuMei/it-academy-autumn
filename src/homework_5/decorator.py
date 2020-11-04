"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""


def dec(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        all_ = open("results.txt", 'a')
        all_.write(str(result))
        all_.write('\n')
        all_.close()
        return result
    return wrapper


@dec
def sums(a, b):
    return a + b
