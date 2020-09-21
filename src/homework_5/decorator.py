"""
Создайте декоратор, который хранит результаты вызовы функции
(за все время вызовов, не только текущий запуск программы)
"""


def dec(func):
    var = ()

    def wrapper(*args, **kwargs):
        nonlocal var
        result = func(*args, **kwargs)
        var += (result,)
        return var
    return wrapper


@dec
def sums(a, b):
    return a + b


print(sums(5, 9))
print(sums(2, 6))
print(sums(9, 9))



