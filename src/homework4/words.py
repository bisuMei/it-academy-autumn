"""
Во входной строке записан текст.
Словом считается послед. непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами
конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


def words(string_):
    """

    :param string_:
    :return: int
    """

    min_word_len = 2
    words_lst = string_.split()

    for word in words_lst:
        if len(word) < min_word_len:
            words_lst.remove(word)

    set_of_words = set(words_lst)

    return len(set_of_words)
