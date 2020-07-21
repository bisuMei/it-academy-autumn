"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Palindrom

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    num_0 = n
    num_1 = 0
    result_num = 0

    while num_0 > 0:
        num_1 = num_0 % 10
        num_0 //= 10
        result_num *= 10
        result_num += num_1

    if result_num == n:
        return True
    else:
        return False


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 5456
    print(palindrom(n))
