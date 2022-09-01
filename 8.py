# list = ["a1","a2","a3","a4"]
# list2 = [i [::-1] for i in list]
# print(list2)


# names = ['Max', 'Helen', 'Alex',
# 'Misha']
# list_a = [name for name in names if 'a' in name]
# ['Max', 'Misha']
# print(list_a)
# n = int(input())
# car = [ {'serial_n':123456, 'year':1995, 'mark':'mazda'},  {'serial_n':54321, 'year':1994, 'mark':'bmw'} ]
# n1 = [i for i in car if i["year"] > n]
# for i in car:
#     if i['year'] > n:
#         n1.append(i)
# print(n1)
# from random import randint
# n = 3
# matrix = [[randint(1, 9) for j in range(n)] for i in range(n)]
# old_dict = {'aa': "1", 'b': "2", 'cccc': "3"}
# new_dict = {value:key for key,value in old_dict.items() }
# print(new_dict)
# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# def yr(a,b,c):
#     res = 0
#     res2 = 0
#     d = b**2 - 4 * a * c
#     print(d)
#     if d == 0:
#         res = -b /2*a
#     elif d > 0:
#         res = (-b +((b**2 - 4 * a * c) / 0.5)) / (2 * a)
#         res2 = (-b -((b**2 - 4 * a * c) / 0.5)) / (2 * a)
#     else:
#         res = "Корней нет"
#     if res2:
#         return res,res2
#     else:
#         return res,"Второго Корня нет"
    
# res_f,res_s = yr(a,b,c)
# print(f'{res_f},\n{res_s}'
n = [1,2,3,4,5,6,7,8,9,10]
n1 =2
res =[]

    
def is_power_n( k:int , n:int)->bool:
    res = k % n
    if res == 0:
        return True
    else:
        return False
for i in n:
    g = is_power_n(i,n1)
    if g == True:
        res.append(i)
print(res)
    
    


        


    


        


