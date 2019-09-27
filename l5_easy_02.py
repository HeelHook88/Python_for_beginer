import os

def ls_dir ():
    print(os.listdir(os.getcwd()))

if __name__ == '__main__':
    ls_dir()