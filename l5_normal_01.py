import os
import shutil as sh_u
import sys
from lection_5.l5_easy_02 import ls_dir
from lection_5.l5_easy_01 import delete_dir
from lection_5.l5_easy_01 import create_dir


def change_directory ():
    try:
        name_dir = input('Введите имя директории ')
        os.chdir(name_dir)
        print("перешел в директорию ")
    except:
        print('не возможно перейти ')

def look_dir ():
    ls_dir()


def del_dir ():
    try:
        delete_dir()
        print('Директории удалены ')
    except:
        print("Невозможно удалить ")


def create_dir ():
    try:
        create_dir()
        print("Директория создана ")
    except:
        print("Невозможо создать ")

def user_choise(choise):
    if choise == 1 :
        change_directory()
    elif choise == 2 :
        look_dir()
    elif choise == 3 :
        delete_dir()
    elif choise == 4 :
        create_dir()

def start():
    while True:
        choice = int(input( 'Выберите пункт:\n'                  
                                '1. Перейти в папку\n'
                                '2. Просмотреть содержимое текущей папки\n'
                                '3. Удалить папку\n'
                                '4. Создать папку\n'
                                '5. Закончить работу\n'   
                                '---------------------\n'))

        if  choice == 5:
            print('До встречи')
            sys.exit()
        else:
            user_choise(choice)

if __name__ == '__main__':
    start()