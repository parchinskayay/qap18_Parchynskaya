# qap18_Parchynskaya_HW3

# 1.Привести к целому типу - 1.6, 2.99

a = 1.6
b = 2.99

a_int = int(a)
b_int = int(b)

print(a, " int: ", a_int, "\n", b, " int: ", b_int, sep="")

# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

str1 = 'www.my_site.com#about'

str1_repl = str1.replace("#", "/")

print(str1_repl)

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

str1 = "stroka"
str2 = "ing"

result = str1 + str2

print(result)

# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

str2 = "Ivanou Ivan"

surname, first_name = str2.split(" ")
result = first_name + " " + surname

print(result)

# 5 Напишите программу которая удаляет пробел в начале, в конце строки

str2 = " Hello "

str_del = str2.strip()

print(str_del)

# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые
# бы отражали количество учащихся в
# десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

school = {"1а": 28,
          "1б": 27,
          "2б": 7,
          "6a": 26,
          "7в": 5,
          "8а": 14,
          "9б": 21,
          "10б": 17,
          "11г": 13,
          "12в": 15}

print(school)

# 7 Создайте список и извлеките из него списка второй элемент.

cars = ["Opel", "KIA", "BMW", "Audi"]

print(cars[2])

# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )

str1 = "employ"
str2 = "employment"

pos = str2.find(str1)

if pos != -1:
    print("Yes")
else:
    print("No")

# 9 Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt

x = "My name is Agent Smith"

print(x[1])   # y
print(x[3:18:3])   # nesgt

# 10 Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

a = [1, 5, 2, 9, 2, 9, 1]

for e in a:
    if a.count(e) == 1:
        print(e)
