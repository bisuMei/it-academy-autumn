"""
Даны два натуральных числа.
Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

a = 1071
b = 462

while a and b:
    if a > b:
        a = a % b
    else:
        b = b % a
# if module not a zero, it is common delimiter
if a > b:
    print(a)
else:
    print(b)
