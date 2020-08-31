"""
Уникальные элементы в списке
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""


def unique(lst_):
    """Unique

    :param lst_:
    :return: list of unique elements
    """
    dict_ = {}
    result = []

    for i in lst_:
        dict_[i] = dict_.get(i, 0) + 1

    for key, value in dict_.items():
        if value == 1:
            result.append(key)
    return result
