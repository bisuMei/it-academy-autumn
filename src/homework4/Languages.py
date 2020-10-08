"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""

students_dict = {}
all_languages = []
lst_language = []
all_lang = set()
all_known = set()


n = input("Enter amount of students: ")

for i in range(int(n)):
    m = input("Number of {} student languages: ".format(i + 1))
    for x in range(int(m)):
        languages = input("Enter {} language of {} student: "
                          .format(x + 1, i + 1))
        lst_language.append(languages)
        students_dict[i + 1] = lst_language[:]
    lst_language.clear()

for languages in students_dict.values():
    all_lang, all_known = set(languages), all_lang
    all_known = all_known & all_lang
    all_languages.extend(languages)

rear_known = set(all_languages) - all_known


print(len(all_known))

print(list(all_known))

print(len(rear_known))

print(list(rear_known))
