# 1. Присвойте двум переменным любые числовые значения.

a = 10
b = 20

print(a, b)

# 2. Составьте четыре сложных логических выражения с помощью оператора and,
# два из которых должны давать истину, а два других - ложь.

print(a == 10 and b == 20, a > 3 and b < 40, a <= 15 and b < 10, a <= 10 and b >= 100)

# 3. Аналогично выполните п. 2, но уже используя оператор or.

print(a == 10 or b == 20, a > 3 or b < 40, a >= 15 or b < a, a < 10 or b >= 100)

# 4. Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.

print("a" == "a" and "b" != "c")