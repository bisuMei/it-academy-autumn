"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def pairs(string):
    """Pairs

    :param string: delimiter whitespace
    :return: number of pairs
    """
    count_pairs = 0
    lst_ = string.split()
    while lst_:
        for i in range(1, len(lst_)):
            if lst_[0] == lst_[i]:
                count_pairs += 1
        lst_.remove(lst_[0])
    return count_pairs
