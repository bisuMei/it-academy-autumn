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


def popular_words(string, list_):
    """Popular words

    :param string:
    :param list_:
    :return: The dict where the search words are the keys and values
             are the number of times when those words are occurring
             in a given text.
    """

    count_pop_words = {}
    str_lowercase = string.lower()
    list_of_str_words = str_lowercase.split()
    for word in list_:
        count_pop_words.update({word: list_of_str_words.count(word)})
    return count_pop_words


# Example:
# print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'nearly', 'wtf']))


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
        num_x = lst[-1 + i]
        num_y = lst[i]
        if len(lst) < 2:
            break
        elif num_x < num_y:
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
    lst_.extend(new_str)

    for i in lst_:
        count = new_str.count(i)
        dict_[i] = count
    for value in dict_.values():
        if value > 1:
            return False
    return True


"""
Write Morse decoder
While the Morse code is now mostly superseded by voice and digital data
communication channels, it still has its use in some applications around
the world. The Morse code encodes every character as a sequence of "dots"
and "dashes". For example, the letter A is coded as ·−, letter Q is coded
as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive,
traditionally capital letters are used. When the message is written in Morse
code, a single space is used to separate the character codes and 3 spaces are
used to separate words. For example, the message HEY JUDE in Morse code is
···· · −·−−   ·−−− ··− −·· ·.
NOTE:
Extra spaces before or after the code have no meaning and should be ignored.
In addition to letters, digits and some punctuation, there are some special
service codes, the most notorious of those is the international distress signal
SOS(that was first issued by Titanic), that is coded as ···−−−···.
These special codes are treated as single special characters, and usually are
transmitted as separate words.

Your task is to implement a function that would take the morse code as input
and return a decoded human-readable string.
"""


def decode_morse(morse_code):
    """Decoder

    :param morse_code:
    :return: human-readable string
    """
    chart_of_morse = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                      'SOS': '...---...'}

    # chars_for_word is a symbols after encoded
    chars_for_word = []
    encoded_words = []
    # as 3 spaces are used to separate words, split morse code by morse words
    split_by_morse_words = morse_code.split('   ')
    for i in range(len(split_by_morse_words)):
        morse_word = split_by_morse_words[i].split()
        for symbol in morse_word:
            if symbol.isalnum():
                chars_for_word.append(" " + symbol + " ")
            for char, morse in chart_of_morse.items():
                if symbol == morse:
                    chars_for_word.append(char)
        encoded_words.append("".join(chars_for_word))
        chars_for_word.clear()
    result = " ".join(encoded_words)
    return result.strip()


# Example:
print(decode_morse('.... . -.--   .--- ..- -.. .'))


"""
Sun Angle:
Your task is to find the angle of the sun above the horizon knowing the time
of the day.
Input data:
the sun rises in the East at 6:00 AM, which corresponds to the angle
of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle
equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".
"""


def sun_angle(time):
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

# Example:
# print(sun_angle('12:14'))
