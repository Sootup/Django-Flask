""" 1111111
x = int(input("Введите первое число:"))
y = int(input("Введите второе число:"))
s = input("Введите знак:")
while True:
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

""" 22222222
n = int(input("Введите число:"))
s = 0 
m = 1
while n > 0:

print("Сумма:",s)
print("Произведение:",m)
"""



    