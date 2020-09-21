"""
Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def closes(num):
    extend = 1
    two = 2
    result = 0
    if num == 1:
        return 1
    while result < num:
        result = two << extend
        if result < num:
            close_before = result
        else:
            close_after = result
        extend += 1
    diff_1 = num - close_before
    diff_2 = close_after - num
    if diff_1 < diff_2:
        return close_before
    else:
        return close_after


"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def delimiter(num):
    delim = 1
    max_delim = 0
    rest = 0

    while rest == 0:
        max_delim = delim
        delim = delim << 1
        rest = num % delim

    return max_delim


print(delimiter(16))
