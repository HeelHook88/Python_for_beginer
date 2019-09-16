import random

leight_list = int(input('Введите волличество элементов в списке:\n'))

new_list = []

while len(new_list) < leight_list:
    new_list.append(random.randint(-100, 100))

print(new_list)