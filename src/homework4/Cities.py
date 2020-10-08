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

countries_lst = []

common_dict = {}

for i in range(int(n)):
    countries_lst = input("Enter country with cities: ").split()
    for city in countries_lst[1:]:
        common_dict.setdefault(countries_lst[0], []).append(city)

m = input("Enter amount of requires: ")

for i in range(int(m)):
    city_ = input("Enter name of a city: ")
    for country, list_of_cities in common_dict.items():
        if city_ in list_of_cities:
            print(country)
