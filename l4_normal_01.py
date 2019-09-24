import re

def check_upper_name (name):
    if re.match(pattern_01, name):
        print(name ,'Имя указано верно ')
    else:
        print(name, 'Имя введенно не правильно')

def check_upper_surname(surname):
    if re.match(pattern_01, surname):
        print(surname ,'Фамилия указана верно ')
    else:
        print(surname,  'Фамилия  введенна не правильно')

def check_mail (email):
    if re.match(pattern_02,email):
        print(email, 'Почта указана верно ')
    else:
        print(email, 'Почта указана в не правильном формате')

name = input('Введите Ваше имя : ')
surname = input('Введите вашу фамилию : ')
email = input('Введите ваш email : ')

pattern_01 = '(^[A-Z,А-Я])'
pattern_02 = '[a-z,_,0-9 ]+@[a-z]+\.(ru|org|com)'

check_upper_name(name)
check_upper_surname(surname)
check_mail(email)