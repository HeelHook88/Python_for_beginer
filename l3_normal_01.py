
names = ['Andrey', 'Anatoliy', 'Nikolai','Evgeniy']
solarys = [30000, 20000, 40000, 39000]
result = {}

names = map(lambda x:x.upper(), names)
result = str(dict(zip(names,solarys)))


with open('salary.txt', 'w', encoding='utf-8') as file:
    file.writelines(result)

with open('salary.txt', 'r', encoding='utf-8') as file:
    work = file.readlines()

work = work