"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
"""

students_dict = {}
count_language = {}
all_known = []
rear_known = []
quantity_all_known = 0
quantity_rear_known = 0
lst_language = []

n = input("Enter amount of students: ")
for i in range(int(n)):
    m = input("Number of {} student languages: ".format(i + 1))
    for x in range(int(m)):
        languages = input("Enter {} language of {} student: "
                          .format(x + 1, i + 1))
        lst_language.append(languages)
        students_dict[i + 1] = lst_language[:]
    lst_language.clear()

for languages_ in students_dict.values():
    for language in languages_:
        count_language[language] = count_language.get(language, 0) + 1

for key, value in count_language.items():
    if count_language[key] == int(n):
        quantity_all_known += 1
    else:
        quantity_rear_known += 1

while count_language:
    name = max(count_language, key=lambda x: count_language[x])
    if count_language[name] == int(n):
        all_known.append(name)
    else:
        rear_known.append(name)
    count_language.pop(name)

print(quantity_all_known)

print(all_known)

print(quantity_rear_known)

print(rear_known)
