"""Посчитать количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.
"""


def count_letters(str_):
    """Подсчет символов.

    :param str_: входная строка
    :return: кортеж. (low_number, up_number). low_number - количество строчных,
                                              up_number - количество прописных.
    """

    # write your code here
    low_number = 0
    up_number = 0

    alph = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ
              abcdefghijklmnopqrstuvwxyz'''

    str_lst = []

    for letter in alph:
        for i in str_:
            if letter is i:
                str_lst.append(letter)

    new_str = "".join(str_lst)

    for i in new_str:
        if i.islower():
            low_number += 1
        elif i.isupper():
            up_number += 1

    return (low_number, up_number)  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(count_letters(str_))
