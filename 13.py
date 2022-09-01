# class Counter:
#     __res = 0
#     def __init__(self,counter):
#         self.counter = counter
    
#     @classmethod
#     def atribute(cls):
#         return cls.__res 

    
#     @staticmethod
#     def get_random_name(number):
#         return number > 3


# first = Counter(1)
# print(Counter.atribute())
# print(Counter.get_random_name(first.counter))

# a = input('a: ')
# b = input('b: ')
# try:
#     result = int(a) / int(b)
# except ZeroDivisionError as err:
#     print(f'b is zero - {err}!!!')
# except Exception as err:
#     print(f'SOMETHING WRONG - {err}!!!')
# finally:
#     print('Сработает всегда' )




class My_errors(Exception):
    def __init__(self,message = "You are right!" ):
        super().__init__(message)


class Book(My_errors):
    def __init__(self,pages,year,author,price):
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price

    
    @staticmethod
    def inputs():
        pages = input()
        year = input()
        author = input()
        price = input()
        return pages,year,author,price


page,year,author,price = Book.inputs()
print(page,year,author,price)

try:
    if page.isdigit():
        raise  My_errors
except My_errors as err:
    print("error")
    