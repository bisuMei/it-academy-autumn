"""
First word:
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:
    There can be dots and commas in a string.
    A string can start with a letter or, for example, a dot or space.
    A word can contain an apostrophe and it's a part of a word.
    The whole text can be represented with one word and that's it.
"""


def first_word(string):
    """First word

    :param string
    :return: string
    """

    new_str = ''
    n1 = ''
    for i in string:
        if i.isalpha() or i.isspace() or i == '\'' or i == '.':
            new_str += i
        else:
            continue
    n1 = new_str.replace('.', ' ')
    new_lst = n1.split()

    return new_lst[0]


"""
Checkio:
You are given a non-empty list of integers (X).
For this task, you should return a list consisting
of only the non-unique elements in this list.
To do so you will need to remove all unique
elements (elements which are contained in a given
list only once). When solving this task, do not
change the order of the list. Example: [1, 2, 3, 1, 3]
1 and 3 non-unique elements
and result will be [1, 3, 1, 3].
"""


def checkio(list):
    """Checkio

    :param list
    :return: An iterable of integers.
    """

    new_list = []
    for i in list:
        if list.count(i) > 1:
            new_list.append(i)

    return new_list


"""
Popular words:
In this mission your task is to determine the popularity
of certain words in the text. At the input of your function
are given 2 arguments: the text and the array of words
the popularity of which you need to determine.

When solving this task pay attention to the following points:
The words should be sought in all registers.
This means that if you need to find a word "one" then words like:
"one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned
in the dictionary with 0 (zero) value.
"""


def popular_words(string, list):
    """Popular words

    :param string:
    :param list:
    :return: The dict where the search words are the keys and values
             are the number of times when those words are occurring
             in a given text.
    """

    my_dict = {}
    new_str = string.lower()
    split_list = new_str.split()
    for x in list:
        my_dict.update({x: split_list.count(x)})
    return my_dict

# print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'nearly']))


"""
Ascending list:
Determine whether the sequence of elements items is ascending
so that its each element is strictly larger than
(and not merely equal to) the element that precedes it.
"""

def is_ascending(lst):
    """Ascending list

    :param lst:
    :return: bool
    """

    for i in range(1, len(lst)):
        n = lst[-1+i]
        k = lst[i]
        if len(lst) < 2:
            break
        elif n < k:
            continue
        else:
            return False
    return True


"""
Isogram:
An isogram is a word that has no repeating letters,
consecutive or non-consecutive. Implement a function
that determines whether a string that contains only
letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(string):
    """Isogram

    :param string
    :return: bool
    """
    new_str = string.lower()
    lst_ = []
    dict_ = {}
    count = 0
    lst_.extend(new_str)

    for i in lst_:
        count = new_str.count(i)
        dict_[i] = count
    for value in dict_.values():
        if value > 1:
            return False
    return True