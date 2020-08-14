"""
1) Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2) Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
3) Используйте генератор списков чтобы получить следующий:
['1a', '2a', '3a', '4a'].
4) Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5) Скопируйте список и добавьте в него элемент '2a' так
чтобы в исходном списке этого элемента не было.
"""

# 1)
lst = ['a', 'b', 'c', 'd']
new_lst = [list(lst[i]+chr_ for chr_ in lst[1:])for i in range(2)]
result = new_lst[0] + new_lst[1]
print(result)
# 2)
print(result[::2])
# 3)
nums = [1, 2, 3, 4]
chr_ = "a"
final = [str(num)+chr_ for num in nums]
print(final)
# 4)
print(final.pop(final.index("2a")))
# 5)
copy_lst = final[:]
copy_lst.append('2a')
print(copy_lst)