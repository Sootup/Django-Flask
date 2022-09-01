import random as r


class Matrix:
    def __init__(self,data,n = 5,m = 5,random_number = r.randint(1,9)):
        self.data = data
        self.n = n
        self.m = m
        self.random_number = random_number


    def max_matrix(self):
        maxx = self.data[0][0]
        for i in self.data:
            for g in i:
                if g > maxx:
                    maxx =g
        return maxx


    def min_matrix(self):
        minn = self.data[0][0]
        for i in self.data:
            for g in i:
                if g < minn:
                    minn =g
        return minn
    
    def summ_matrix(self):
        summ = 0
        for i in self.data:
            for g in i:
                summ += g
            
        return summ
    
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.data])

    @staticmethod
    def make_matrix(n1=5,n2=5,random1 = 0,random2= 0):
        ar1 = [[0]*n1 for _ in range(n2)]
        if random1 != 0 or random2 != 0:
            for i in range(n1):
                for g in range(n2):
                    ar1[i][g] = r.randint(random1,random2)
        return ar1
    
