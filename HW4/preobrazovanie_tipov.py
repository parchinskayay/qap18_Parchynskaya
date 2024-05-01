# 1 Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love",
# "arrays", "they", "are", "my", "favorite"]

str1 = "Robin Singh"
str2 = "I love arrays they are my favorite"

list1 = str1.split()
list2 = str2.split()

print(list1, list2)

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

list_name = ["Ivan", "Ivanou"]
str3 = "Minsk"
str4 = "Belarus"

print("Привет, " + " ".join(list_name) + "! Добро пожаловать в " + str3, str4)

# 3.Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него
# строку => "I love arrays they are my favorite"

my_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]

print(" ".join(my_list))

# 4.Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

elements = ["а", "б", "в", "г", "д", 1, 2, 3, 4, 5]

elements[:2] += "e"
elements.pop(6)

print(elements)

# 5. Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

c = {}
for key in a:
    c[key] = [a.get(key), b.get(key)]
for key in b:
    c[key] = [a.get(key), b.get(key)]
print(c)
