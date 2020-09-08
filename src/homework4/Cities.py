"""
Дан список стран и городов каждой страны. Затем даны назв. городов.
Для каждого города укажите, в какой стране он находится.
Входные данные:
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. В следующей строке записано число M, далее идут
M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные:
Для каждого из запроса выведите название страны,
в котором находится данный город.
"""


n = input("Enter amount of countries: ")
common_dict = {}

for i in range(int(n)):
    countries = input("Enter country with cities: ")
    countries_lst = countries.split()
    for city in countries_lst[1:]:
        common_dict[city] = common_dict.get(city, countries_lst[0])

m = input("Enter amount of requires: ")

for i in range(int(m)):
    cities = input("Enter name of city: ")
    for key, value in common_dict.items():
        if cities == key:
            print(value)
