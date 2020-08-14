"""
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""

# version 1
for i in range(1, 101):
    if not i % 15:
        print("FizzBuzz")
    elif not i % 3:
        print("Fizz")
    elif not i % 5:
        print("Buzz")
    else:
        print(i)

# version 2
fizzbuzz = [('fizz'*(not i % 3) + 'buzz'*(not i % 5) or i)
            for i in range(1, 101)]