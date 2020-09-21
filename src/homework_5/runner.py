import all_hw_in_func as my_mod
"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
runner() – все фукнции вызываются по очереди.
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции.
"""


def runner(*args):
    if not args:
        func_names = [name for name in dir(my_mod) if name[0] != '_']
    else:
        func_names = [*args]
    for name in func_names:
        if hasattr(my_mod, name):
            func = getattr(my_mod, name)
            print(func())
        else:
            print("This func {} not found".format(name))
    return ''


runner()
