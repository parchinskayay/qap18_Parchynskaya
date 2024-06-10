import os
import re


def check_tags_in_file(path):
    """функция читает файлы построчно, проверяет, что все открывающиеся html теги:
     p, button, h2, h, имеют метку i18n"""
    has_error = False
    error_lines = {}
    with open(path) as f:
        lines = f.readlines()
        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            tags = re.findall(r'<[^/].*?>', line)
            """составляем регулярные выражения для поиска открывающихся тегов"""
            for tag in tags:
                if ('p' in tag[1] or 'button' in tag[1:7] or 'h' in tag[1]
                    or 'h2' in tag[1:3]) and tag.find('i18n') == -1:
                    error_lines[line_num] = line
                    has_error = True
            line_num += 1
    if has_error is True:
        print(path)
        for num, line in error_lines.items():
            print(f"{num}: {line}")


def check_tags_in_dir(cur):
    """функция рекурсивно проходит по директории и для файлов, имеющих расширение
    html вызывает функцию check_tags_in_file"""
    for dr in os.listdir(cur):
        """игнорируем директорию .git"""
        if dr == ".git":
            continue
        abs_path = os.path.join(cur, dr)

        if os.path.isdir(abs_path):
            check_tags_in_dir(abs_path)
        elif 'html' in dr[-4:]:
            check_tags_in_file(abs_path)


check_tags_in_dir(r'test-i18n')
