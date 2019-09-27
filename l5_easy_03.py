import os
import shutil as sh

def copy_run_file():
    sh.copy(__file__,path)


if __name__ == '__file__':

    try:
        path = 'copy_scrypt'
        os.mkdir(path)
        copy_run_file()
    except FileExistsError:
        print('файл скопирован и находится в папке copy_scrypt')