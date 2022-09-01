from functools import reduce
ma = [1,2,3]
result = reduce(lambda a, x: a * x , filter(lambda a:  not a % 3 , ma))
print(result)