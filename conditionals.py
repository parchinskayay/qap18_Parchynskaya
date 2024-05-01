# 1 Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число.

a = 2

if a > 0:
    a += 1

print(a)

# 2 Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.

a = [1, 4, -2]
count = 0

for x in a:
    if x > 0:
        count += 1

print(count)

# 3. Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются).


year = 2024

if year % 400 == 0:
    print("366")
elif year % 100 == 0:
    print("365")
elif year % 4 == 0:
    print("366")
else:
    print("365")

# 4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).

a = 3

week_days = {1: "понедельник", 2: "вторник", 3: "среда", 4: "четверг",
             5: "пятница", 6: "суббота", 7: "воскресенье"}

print(week_days[a])


if a == 1:
    print("понедельник")
elif a == 2:
    print("вторник")
elif a == 3:
    print("среда")
elif a == 4:
    print("четверг")
elif a == 5:
    print("пятница")
elif a == 6:
    print("суббота")
elif a == 7:
    print("воскресенье")

# 5. Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер едини- цы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах.

a = 5
b = 0.65

if a == 1:
    print(b)
elif a == 2:
    print(b / 1000000)
elif a == 3:
    print(b / 1000)
elif a == 4:
    print(b * 1000)
elif a == 5:
    print(b * 100)