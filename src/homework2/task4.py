"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
"""


def count_letters(string):
    """Подсчет символов.

    :param string: входная строка
    :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                              up_number - количество прописных.
    """

    # write your code here
    low_number = 0
    up_number = 0

    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    str_lst = [letter for letter in string if letter in alph]

    for letter in str_lst:
        if letter.islower():
            low_number += 1
        else:
            up_number += 1

    return low_number, up_number  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(count_letters(str_))
