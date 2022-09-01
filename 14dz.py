import os

# name = input("Введите имя папки:")
# file_path = os.path.realpath( __file__)
# dir_name = os.path.dirname(file_path)
# os.mkdir(name)




# dir_name = input("Введите имя папки:")
# file_name = input("Введите имя файла:")
# os.mkdir(dir_name)
# filepath = os.path.join(f'/home/ub/Документы/lessons/Python_lessons/{dir_name}', file_name)
# my_file = open(filepath, "a")
# my_file.close()

text = [ "def main():"\n,
         "\tpass"\n,
         "if __name__ == '__main__' :"\n,
         "\tmain()" ]

dir_name = input("Введите имя папки:")
file_name = input("Введите имя файла:")
os.mkdir(dir_name)
filepath = os.path.join(f'/home/ub/Документы/lessons/Python_lessons/{dir_name}', file_name)
my_file = open(filepath, "a")
if ".py" in file_name:
    zapis =open(my_file, "a"):
        writelines
my_file.close()





# def main():
#     pass
# if __name__ == '__main__' :
#     main()

























# file = open(file_name,"a")
# file.close()
# file_path = os.path.realpath( __file__)
# dir_name = os.path.dirname(file_path)
# print(os.getcwd())