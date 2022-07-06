"""
s = [1,2,3,4,5]
for i in s:
    print(i * -2)
"""


"""
s = [1,2,3,4,5,6,7,8]
s2 = 0
for i in s:
    if i % 2:
        s2 += 1
print(s2)
""" 


"""
a ={'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(a.keys()):
    a[key + str(len(key))] = a.pop(key)
print(a.keys())
"""


"""
a = [1,2,3,4,5]
a.pop(0)
a.extend("1")
print(a)
"""

"""
f1 = f2 = 1
print("Список чисел фибоначи до 15:")
print(f1,"", f2, end=" ")
for i in range(0,13):
    f1,f2 = f2,f1 + f2
    print("",f2,end=" ")
"""
