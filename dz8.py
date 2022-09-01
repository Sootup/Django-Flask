n = int(input("Введите число для нахождения его двойного факториала:"))
res = 1
while n == 1:
    print(res)
    break
for i in range(n):
    if n % 2 == 0:
        res *= i
print(res)
    
  

