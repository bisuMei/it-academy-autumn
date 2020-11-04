"""
Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def closes(num):
    binary_shift = 1
    power_of_two = 0
    if num == 1:
        return 1
    if num == 2:
      return 2
    while power_of_two < num:
        power_of_two = 1 << binary_shift
        if power_of_two < num:
            closest_before_num = power_of_two
        else:
            closest_after_num = power_of_two
        binary_shift += 1
    diff_1 = num % closest_before_num
    diff_2 = closest_after_num % num
    if diff_1 < diff_2:
        return closest_before_num
    else:
        return closest_after_num


"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def delimiter(num):
    power_of_two = 1
    max_delimiter = 0
    rest = 0

    while rest == 0:
        max_delimiter = power_of_two
        power_of_two = power_of_two << 1
        rest = num % power_of_two

    return max_delimiter
