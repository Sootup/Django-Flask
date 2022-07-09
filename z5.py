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