def total_sum(m=10, n=12, s=4):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    total = str((m + n / 100) * s).split('.')
    return "{0} rubles {1} kopecks".format(total[0], int(total[1]))


def longest_word(str_='Super longggest'):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """

    lst = []
    longest = ''

    lst.extend(str_)
    punctuation = "!#$%\"&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for quote in punctuation:
        lst = [i.replace(quote, ' ') for i in lst]

    new_str = ''.join(lst)

    lst_1 = new_str.split()

    for i in lst_1:
        if len(longest) < len(i):
            longest = i

    return longest


def palindrom(n=525):
    """Palindrom

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    num_0 = n
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


def sun_angle(time='15:24'):
    """Sun Angle

    :param time: The time of the day
    :return: The angle of the sun, rounded to 2 decimal places.
    """
    t_lst = time.split(':')
    # one_h_ang and one_m_ang - angles hour and minute
    one_h_ang = 15
    one_m_ang = 0.25
    if int(t_lst[0]) == 18 and int(t_lst[1]):
        return "I don't see the sun!"
    elif 6 <= int(t_lst[0]) <= 18:
        sun_angl_ = (int(t_lst[0]) - 6) * one_h_ang + int(t_lst[1]) * one_m_ang
        return sun_angl_
    else:
        return "I don't see the sun!"


def pairs(string='1 1 1 1'):
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
