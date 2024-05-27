# 1 Создать lambda функцию, которая принимает на вход имя и выводит его
# в формате “Hello, {name}”.

greeting = lambda name: f"Hello, {name}"
print(greeting("Julia"))

# 2 Создать lambda функцию, которая принимает на вход список имен и
# выводит их в формате “Hello, {name}” в другой список.

hello_girls = lambda names: list(map(lambda y: f"Hello, {y}", names))
girls = ("Маша", "Даша", "Саша", "Катя")
print(hello_girls(girls))


# 3. Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# и возвращает новый список только с положительными числами.

def create_generator():
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    for num in numbers:
        if num > 0:
            yield num


my_generator = create_generator()
# print(next(my_generator))

for x in my_generator:
    print(x)

# 4.Необходимо составить список чисел которые указывают на длину слов в строке:
# sentence = "" thequick brown fox jumps over the lazy dog"",
# но только если слово не ""the"" с обработкой исключений.


class MyException(Exception):
    pass


sentence = "thequick brown fox jumps over the lazy dog"
words_len = []
try:
    for word in sentence.split():
        if word == "the":
            raise MyException
        else:
            words_len.append(len(word))
except MyException:
    print("Exception")

print(words_len)

# 5.Шифр Цезаря * — один из древнейших шифров. При шифровании каждый символ
# заменяется другим, отстоящим от него в алфавите на
# фиксированное число позиций.(например на 3, то есть +3
# Примеры:
# abc -right> bcd  encoding
# bcd -left>  abc    decoding
# ● hello world! -> khoor zruog!
# ● this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# " то есть кодирует и декодирует текст

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encode(s, shift):
    encode_str = ""
    for i in s:
        index = alphabet.find(i)
        if index != -1:
            new_index = (index + shift) % len(alphabet)
            encode_str += alphabet[new_index]
        else:
            encode_str += i
    return encode_str


def decode(s, shift):
    decode_str = ""
    for i in s:
        index = alphabet.find(i)
        if index != -1:
            new_index = (index - shift) % len(alphabet)
            decode_str += alphabet[new_index]
        else:
            decode_str += i
    return decode_str


sh = 3
enc_str = encode("hello world!", sh)
print(enc_str)
print(decode(enc_str, sh))

sh = 5
enc_str = encode("this is a test string", sh)
print(enc_str)
print(decode(enc_str, sh))
