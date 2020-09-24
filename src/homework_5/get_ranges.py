"""
Реализовать функцию get_ranges которая получает на вход
непустой список неповторяющихся целых чисел, отсортированных
по возрастанию, которая этот список “сворачивает”
"""

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
# get_ranges([4,7,10]) // "4,7,10"
# get_ranges([2, 3, 8, 9]) // "2-3,8-9"


def get_ranges(lst_):
    """Get ranges

    :param lst_:
    :return string
    """

    final_str = ""
    lst_of_nums = []
    lst_with_sequence = []
    copy_lst_of_nums = []
    previous_diff = 0

    for i in range(len(lst_) - 1):
        # diff_ is a difference between current and next number
        current_diff = lst_[i + 1] - lst_[i]
        # check nums for sequence
        if current_diff == 1:
            lst_of_nums.append(lst_[i])
            lst_of_nums.append(lst_[i + 1])
            copy_lst_of_nums = lst_of_nums[:]
            previous_diff = current_diff
        else:
            if copy_lst_of_nums not in lst_with_sequence:
                lst_with_sequence.append(copy_lst_of_nums)
            lst_of_nums.clear()
            # check if it is single num in lst, add it to lst
            if previous_diff > 1 and current_diff > 1:
                lst_with_sequence.append(lst_[i])
            previous_diff = current_diff

    lst_with_sequence.append(lst_of_nums)

    # if first or/and last nums are single, add to lst
    if not lst_with_sequence[0]:
        lst_with_sequence[0] = str(lst_[0])
    if not lst_with_sequence[-1]:
        lst_with_sequence[-1] = str(lst_[-1])

    for sequence in lst_with_sequence:
        if type(sequence) is list:
            final_str += " {}-{}".format(sequence[0], sequence[-1])
        else:
            final_str += " " + str(sequence)
    return final_str


print(get_ranges([0, 2, 3, 5, 8, 9, 10, 12]))
