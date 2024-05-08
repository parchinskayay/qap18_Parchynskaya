# 1 Напишите функцию is_year_leap, которая принимает число (год) и возвращает true,
# если год високосный false если нет.

def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


year_console = int(input("Введите год: "))

print(is_year_leap(year_console))


# 2 Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает список, состоящий из
# кубов первых n натуральных чисел.
# То есть [1**3, 2**3, 3**3, ..., n**3]. Обязательно использование генераторов списков.

def generate_natural_cubes(n):
    return [i ** 3 for i in range(n)]


print(generate_natural_cubes(5))


# 3 Напишите функцию generate_squares, которая принимает произвольное количество аргументов и
# возвращает список,состоящий из их квадратов.То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*arg):
    return [i ** 2 for i in arg]


print(generate_squares(1, 2, 3))


# 4 Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста.
# Для разбиения строки на слова используйте функцию split.

# Т.к. явно не указан необходимый результат для случая нескольких слов имеющих максимальную длину.
# Сейчас возвращается только первый элемент для подобных случаев.
def get_longest_word(text):
    words = text.split(" ")
    words_length = list(map(len, words))
    max_el = max(words_length)
    max_ind = words_length.index(max_el)
    return words[max_ind]


print(get_longest_word("AAA bbbBB CCCmmCC"))


# 5* Напишите функцию get_most_frequent_word, которая на вход принимает текст (только
# английские слова и пробелы), и возвращает самое часто встречающееся слово.
# Если таких слов несколько - верните любое.

def get_most_frequent_word(text):
    words = text.split(" ")
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return max(frequency, key=frequency.get)


print(get_most_frequent_word("A B A C"))
