"""Найти самое длинное слово в введенном предложении.

    В случае если их несколько, самое левое в строке Учтите что в предложении
    есть знаки препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    marks = ",./&!@#$%^&*:;"

    lst = []
    lst_1 = []
    longest = ''

    lst.extend(str_)

    for quote in marks:
        lst = [i.replace(quote, '') for i in lst]

    new_str = ''.join(lst)

    lst_1 = new_str.split()

    for i in lst_1:
        if len(longest) < len(i):
            longest = i

    return longest


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(longest_word(str_))
