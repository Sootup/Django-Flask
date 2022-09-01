# class Dog:
#     def __init__(self, height,weight):
#         self.__height = height
#         self.__weight = weight
#     #     self.__age = age
#     #     self.__name = name
#     #     self.__master = master
#     @property
#     def height(self):
#         return self.__height
#     @height.setter
#     def height(self,height):
#         self.__height = height
#     @property
#     def weight(self):
#         return self.__weight
#     @weight.setter
#     def weight(self,weight):
#         self.__height = weight
   
   
    
    # def get_master(self):
    #     return self.__master
    # def set_master(self,master):
    #     self.__master = master
    # def change_name(self,name):
    #     self.name = name
#     def bark(self):
#         print('Woof Woof!')
#     def jump(self):
#         print("Jump!")
#     def run(self):
#         print("Run!")
# dog = Dog("40","15")
# dog.height = "20"
# print(dog.height)
# dog = Dog( 'Alex')
# print(dog.get_master())
# dog.set_master("a")
# print(dog.get_master())

# dog.change_name("Marly")
# dog.bark()
# dog.jump()
# dog.run()
# print(dog.name)


class Pet:

    def __init__(self,weight,height):
        self.weight = weight
        self.height = height

    def change_weight(self,weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.2


    def voice(self):
        pass


    def change_height(self,height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2


    def jump(self,height):

        print(f'jump {height} meters')


    def run(self):
        print("run")


    # def jump(self):
    #     print("jump")


    def birthday(self):
        self.age = self.age + 1
        return self.age
    
    

class Dog(Pet):
    def __init__(self,name, age, master):
        self.name = name
        self.age = age
        self.master = master

    # def run(self):
    #     print("run")


    # def jump(self):
    #     print("jump")


    # def birthday(self):
    #     self.age = self.age + 1
    #     return self.age

    def jump(self,height):
        super().jump(height)
        if height > 0.5:
            print("Dogs cannot jump so high")
        else:
            print("jump")

    

    def voice(self):
        print("Bark")


class Cat(Pet):
    def __init__(self,name, age, master):
        self.name = name
        self.age = age
        self.master = master

    # def run(self):
    #     print("run")


    # def jump(self):
    #     print("jump")


    # def birthday(self):
    #     self.age = self.age + 1
    #     return self.age
    
    def voice(self):
        print("meow")


class Parrot(Pet):
    def __init__(self,name, age, master,weight,species):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.species = species


    # def run(self):
    #     print("run")


    # def jump(self):
    #     print("jump")


    # def birthday(self):
    #     self.age = self.age + 1
    #     return self.age


    
    def change_weight(self,weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.05



    def change_height(self,height=None):
        if height:
            self.height = height
        else:
            self.height += 0.05



    def fly(self):
        if  self.weight < 0.1:       
            print("Flying bird")
        else:
            print("This parrot cannot fly")

def animals(animals):
    for i in animals:
        i.voice()


dog1 = Dog("Warik",8,"anna")
dog1.jump(0.6)
cat1 = Cat("Waik",8,"anna")
animals([dog1,cat1])

# parrot1 = Parrot("Dabu",2,"anna", 0.045)
# parrot1.fly()
# parrot1.change_weight()
# parrot1.fly()

# dog1.birthday()
# print(dog1.age)

