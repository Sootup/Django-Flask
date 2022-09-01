import json
import csv



# names = ["Igor","denis"]

#  for i in names:
#      name = lambda i: print(f'hello,{i}')
#      name(i)
    
# name = lambda x: [print("hello,"+ name)for name in names]
# name(names)
# result = map(lambda x: x ** 2,
# [1,2,3,4,5,6])
# print(list(result))

# res = map(lambda x: str(x), [1,2,3,4,5,6] )
# print(list(res))

# res = filter(lambda x:"k" in x , ["k","a","d","ka"])
# print(list(res))

# from functools import reduce
# result = reduce(lambda a, x: a + x ** 2, [1,2,3], 0)
# print(result)

# from functools import reduce
# ma = [1,2,3]
# result = reduce(lambda a, x: a * x , filter(lambda a:  not a % 3 , ma))
# print(result)
# from datetime import datetime
# def my_decorator(func):
#     def do_some_staff():
#         time_start = datetime.now()
#         print(time_start)
#         result = func()
#         time_end = datetime.now()
#         print(time_end)
#         res = time_end - time_start
#         print(res)
#         return result
#     return do_some_staff
# @my_decorator
# def my_func():
#     print("hello")
# my_func()
# my_file = open('text.txt')
# res = 0
# while True:
#     line = my_file.readline()
#     if res  >= 0 and res < 5:
#         print(line)
#     res += 1
#     if not line:
#         break    
# my_file.close()
# with open('text.txt', 'a') as my_file:
#     for i in range(1,4):
#         a = input("введите строку:")
#         my_file.write(f'{a}\n')
# with open('text.txt', 'w') as file:
#         with open('test.txt', "r") as file2:
#             for line in file2.readlines():
#                 if '0' in line:
#                     rep = line.replace('0','1')
#                     file.write(rep)
#                 elif '1' in line:
#                     rep = line.replace('1','0')
#                     file.write(rep)
#                 else:
#                     file.write(line)

# with open ("test1.txt", "r") as file:
#     r = 0
#     while True:
#         read = file.readline()
#         r += 1
#         print(read)
#         if r % 2 == 0:
#             with open("test2.txt", "a") as file2:
#                 file2.write(f'{read}\n')
#         else:
#             with open("test3.txt", "a") as file3:
#                 file3.write(f'{read}\n')
#         if not read:
#             break

# res = 0
# with open ("test1.txt", "r") as file:
#     with open("test2.txt", "r") as file2:
#         while True:
#             line1 = file.readline()
#             line2 = file2.readline()
#             res += 1
#             if line1 != line2:
#                 print(res)
#             if not line1 or not  line2:
#                 break


