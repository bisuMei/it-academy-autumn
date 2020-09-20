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

    count_nums = {}
    result = []
    lst = string.split()
    for num in lst:
        count_nums[num] = count_nums.get(num, 0) + 1

    for amount in count_nums.values():
        pairs = amount * (amount - 1) // 2
        result.append(pairs)

    return sum(result)
