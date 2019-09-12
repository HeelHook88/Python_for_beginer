name = input('Введите ваше имя ')
surname = input('Введите вашу фамилию ')
age = int(input('Введите ваш возраст '))
weight = int(input('Введите ваш вес '))
if age <= 30 and 50 <= weight <= 120:
    print(name, surname, age, "лет", 'вес кг. ', weight, "Хорошее состояние")
elif 30 < age < 40 and weight < 50 or weight > 120:
    print(name, surname, age, "лет", 'вес кг. ', weight, "Следует занятся собой")
elif age > 40 and weight < 50 or weight > 120:
    print(name, surname, age, "лет", 'вес кг. ', weight, "Следует обратится к врачу")
