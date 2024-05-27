# 1 Написать обычную функцию для факториала, генератор и рекурсию.
# Сравнить их время работы
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_generator(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

import time

start_time = time.time()
factorial(10)
print("Время работы обычной функции: ", time.time() - start_time)

start_time = time.time()
factorial(10)
print("Время работы генератора: ", time.time() - start_time)


# 22 Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал:

def typed(type):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                if type == 'str':
                    new_args.append(str(arg))
                elif type == 'int':
                    new_args.append(int(arg))
                else:
                    new_args.append(arg)
            return func(*new_args)
        return wrapper
    return decorator

@typed(type='str')
def add_two_symbols(a, b):
    return a + b

@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c

print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
