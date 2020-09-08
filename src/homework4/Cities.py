"""
Дан список стран и городов каждой страны. Затем даны названия городов.
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
require_cities = []
hash_table = {}

for i in range(int(n)):
    countries = input("Enter country with cities: ")
    countries_lst = countries.split()
    for i in countries_lst[1:]:
        hash_table[i] = hash_table.get(i, countries_lst[0])

m = input("Enter amount of requires: ")

for i in range(int(m)):
    cities = input("Enter name of city: ")
    for key,value in hash_table.items():
        if cities == key:
            print(value)