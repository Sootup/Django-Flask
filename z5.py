"""" 1111
while True:
    x = int(input("Введите первое число:"))
    y = int(input("Введите второе число:"))
    s = input("Введите знак:")
    if s == "0":
        break
    if "+" in s:
        print(x+y)
    elif "-" in s:
        print(x-y)
    elif "*" in s:
        print(x*y)
    elif "/" in s:
        if y != 0:
            print(x/y)
        else:
            print("Деление на ноль")            
    else:
        print("Вы ввели неверный знак")
"""




""" 22222
n = int(input("Введите число:"))
s = 0 
m = 1
while n > 0:   
    d = n % 10
    if d != 0:
        s =  s + d
        m = m * d
    n = n // 10     
print("Сумма:",s)
print("Произведение:",m)
"""


""" 44444
n = int(input("Введите число"))
s = 0
for i in range(1,n + 1):
    s = i + s
print(s)
"""

""" 555
m = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
max = max(m)
for i, n in enumerate(m):
    if i % 2:
        m[i] = max
print(m)
"""

# from random  import randint
# n = 15
# ar = list()
# for i in range(n):
#     r = randint(1,10)
#     ar.append(r)
#     res = 0
#     if i > ar:
#         print(res)


# print(ar)
# print(res)
# num = [1,2,3,4,5]
# def fact2(n):
#     res = 1
#     for i in 
#         res *= i
#     print(res)
    
            


# slova = "bob boba tool"
# def pal(slova):
#     res = []
#     slova = slova.split(" ")
#     # res = "".join(reversed(slova))
#     for i in reversed(slova):
#         res.append(i)
#     return res
# print(pal(slova))


# slova = "bob boba tool"

# def pal(slova):
#     res = []
#     slova = slova.split(" ")
#     for i in range(len(slova)-1,-1,-1):
#         res.append(slova[i])
#     print(res)
        

        
#     return slova


    
  

# print(pal(slova))

# n = int(input("1:"))
# m = int(input("2:"))
# p = range(n,m)
# print(p)
# res = []
# for i in p:
#     for g in range(2, i-1):
#         if i % g == 0:
#             res.append(g)
# print(res)
import datetime
          
num = [{'num':101, 'start':'minsk', 'stop':'brest', 'time_start':datetime.datetime.strptime("02:25","%H:%M"), 'time_end':datetime.datetime.strptime("04:15","%H:%M")},{'num':102, 'start':'gomel', 'stop':'vitebs', 'time_start':datetime.datetime.strptime("01:15","%H:%M"), 'time_end':datetime.datetime.strptime("15:15","%H:%M")}]
for i in num:
    res = i['time_end'] - i["time_start"] 
    if res > datetime.timedelta(hours=7,minutes=20):
        print(i)

