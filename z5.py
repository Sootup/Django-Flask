"""
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
n = int(input("Введите число"))
s = 0 
m = 1
while n > 0:
    d = n % 10
    s = s + d
    m = m + d
    n = n // 10
print("Сумма:",s)
print("Произведение:",m)

    