# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку.

f = open("numbers.txt", "r")
v = f.read()
elements = v.split()

if len(elements) < 3:
    print("Error")
else:
    print(elements[0], elements[1], elements[-2], elements[-1])

f.close()


with open("numbers.txt", "r") as file1:
    elements = file1.read().split()

    if len(elements) < 3:
        print("Error")
    else:
        print(elements[0], elements[1], elements[-2], elements[-1])

# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.

f = open("numbers.txt", "r")
v = f.read().split()

f_even = open("even_numbers.txt", "w")
f_odd = open("odd_numbers.txt", "w")

for i in v:
    if int(i) % 2 == 0:
        f_even.write(i + " ")
    else:
        f_odd.write(i + " ")

f.close()
f_even.close()
f_odd.close()

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

f = open("real_numbers.txt", "r")
v = f.read().split()

v2 = [float(i) ** 2 for i in v]

f.close()
f = open("real_numbers.txt", "w")

for i in v2:
    f.write(str(i) + " ")

f.close()

# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа.

with open("bin1.bin", "wb") as f:
    f.write(bytearray([1, 2, 3]))
with open("bin2.bin", "wb") as f:
    f.write(bytearray([4, 5, 6]))

f1 = open("bin1.bin", "rb")
f2 = open("bin2.bin", "rb")

f1_content = f1.read()
f2_content = f2.read()

f1.close()
f2.close()

f1 = open("bin1.bin", "wb")
f2 = open("bin2.bin", "wb")

f1.write(f2_content)
f2.write(f1_content)

f1.close()
f2.close()
