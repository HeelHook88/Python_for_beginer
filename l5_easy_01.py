import os

def create_dir ():
    path_name = input(str('Введите название создаваемых(удаляемых) директорий '))
    num = input('Введите количество создаваемых(удаляемых) директорий ')
    for i in range(int(num)):
        path = '{}{}'.format(path_name, i)
        os.mkdir(path)

def delete_dir ():
    path_name = input(str('Введите название создаваемых(удаляемых) директорий '))
    num = input('Введите количество создаваемых(удаляемых) директорий ')
    for i in range(int(num)):
        path = '{}{}'.format(path_name, i)
        os.rmdir(path)



if __name__ == '__main__':
    print(delete_dir(),os.listdir())