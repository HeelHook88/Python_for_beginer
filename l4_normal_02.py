import re

def check_simbol (some_str):
    if re.search(pattern, some_str):
        print('Совпадения найдены')
    else:
        print('Совпадения не найдены')

pattern = '[...]{3}'

with open('poem.txt', 'r', encoding='utf-8') as file:
    some_str = str(file.readlines())
    check_simbol(some_str)
