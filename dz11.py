
# 222222222222222222222222222222222222
# class Car:
#     def __init__(self,mark,model,year,speed):
#         self.__mark = mark
#         self.__model = model
#         self.__year = year
#         self.__speed = speed


#     @property
#     def mark(self):
#         return self.__mark

#     @mark.setter
#     def mark(self,mark):
#         self.__mark = mark
        
#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self,model):
#         self.__model = model

#     @property
#     def year(self):
#         return self.__year

#     @year.setter
#     def year(self,year):
#         self.__year = year
    
#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self,speed):
#         self.__speed = speed

 
#     def speed_increase(self,speed = 5):
#         if speed:
#             self.__speed += speed
#             return self.__speed
#         else:
#             return self.__speed

#     def speed_decrease(self,speed = speed ):
#         if speed:
#             self.__speed -= 5
#             return self.__speed
#         else:
#             return self.__speed


#     def stop(self,speed = 0):
#         self.__speed = speed
#         print(speed)


#     def show_speed(self):
#         print(self.__speed)
    
        

#     def turn(self):
#         print(-self.__speed)


# car1 = Car("mazda",'zx',2010,0)

# car1.speed_increase()
# car1.speed_decrease()
# car1.speed_increase()
# car1.speed_increase()
# car1.speed_increase()
# car1.speed_increase()
# car1.show_speed()
# car1.turn()
# car1.stop()

######################

# class Pets:
#     def __init__(self,weight,life_expectancy,max_running_speed):
#         self.__weight = weight
#         self.__life_expectancy = life_expectancy
#         self.__max_running_speed = max_running_speed


#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self,weight):
#         self.__weight = weight


#     @property
#     def life_expectancy(self):
#         return self.__life_expectancy
    
#     @life_expectancy.setter
#     def life_expectancy(self,life_expectancy):
#         self.__life_expectancy = life_expectancy


#     @property
#     def max_running_speed(self):
#         return self.__max_running_speed
    
#     @max_running_speed.setter
#     def max_running_speed(self,max_running_speed):
#         self.__max_running_speed = max_running_speed


##############################################


# class Cat:
#     def __init__(self,weight = 8,life_expectancy = 15 ,max_running_speed= 48):
#         self.__weight = weight
#         self.__life_expectancy = life_expectancy
#         self.__max_running_speed = max_running_speed


#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self,weight):
#         self.__weight = weight


#     @property
#     def life_expectancy(self):
#         return self.__life_expectancy
    
#     @life_expectancy.setter
#     def life_expectancy(self,life_expectancy):
#         self.__life_expectancy = life_expectancy


#     @property
#     def max_running_speed(self):
#         return self.__max_running_speed
    
#     @max_running_speed.setter
#     def max_running_speed(self,max_running_speed):
#         self.__max_running_speed = max_running_speed

    


# class Dog:
#     def __init__(self,weight = 20,life_expectancy = 11,max_running_speed= 35):
#         self.__weight = weight
#         self.__life_expectancy = life_expectancy
#         self.__max_running_speed = max_running_speed


#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self,weight):
#         self.__weight = weight


#     @property
#     def life_expectancy(self):
#         return self.__life_expectancy
    
#     @life_expectancy.setter
#     def life_expectancy(self,life_expectancy):
#         self.__life_expectancy = life_expectancy


#     @property
#     def max_running_speed(self):
#         return self.__max_running_speed
    
#     @max_running_speed.setter
#     def max_running_speed(self,max_running_speed):
#         self.__max_running_speed = max_running_speed



# class Rat:
#     def __init__(self,weight= 0.5,life_expectancy = 2,max_running_speed = 10):
#         self.__weight = weight
#         self.__life_expectancy = life_expectancy
#         self.__max_running_speed = max_running_speed


#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self,weight):
#         self.__weight = weight


#     @property
#     def life_expectancy(self):
#         return self.__life_expectancy
    
#     @life_expectancy.setter
#     def life_expectancy(self,life_expectancy):
#         self.__life_expectancy = life_expectancy


#     @property
#     def max_running_speed(self):
#         return self.__max_running_speed
    
#     @max_running_speed.setter
#     def max_running_speed(self,max_running_speed):
#         self.__max_running_speed = max_running_speed



# class Hamster:
#     def __init__(self,weight =0.6,life_expectancy = 2,max_running_speed = 7):
#         self.__weight = weight
#         self.__life_expectancy = life_expectancy
#         self.__max_running_speed = max_running_speed

    
#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self,weight):
#         self.__weight = weight


#     @property
#     def life_expectancy(self):
#         return self.__life_expectancy
    
#     @life_expectancy.setter
#     def life_expectancy(self,life_expectancy):
#         self.__life_expectancy = life_expectancy


#     @property
#     def max_running_speed(self):
#         return self.__max_running_speed
    
#     @max_running_speed.setter
#     def max_running_speed(self,max_running_speed):
#         self.__max_running_speed = max_running_speed



# class Guenia_pig:
#     def __init__(self,weight = 1 ,life_expectancy = 6 ,max_running_speed = 10):
#         self.__weight = weight
#         self.__life_expectancy = life_expectancy
#         self.__max_running_speed = max_running_speed


#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self,weight):
#         self.__weight = weight


#     @property
#     def life_expectancy(self):
#         return self.__life_expectancy
    
#     @life_expectancy.setter
#     def life_expectancy(self,life_expectancy):
#         self.__life_expectancy = life_expectancy


#     @property
#     def max_running_speed(self):
#         return self.__max_running_speed
    
#     @max_running_speed.setter
#     def max_running_speed(self,max_running_speed):
#         self.__max_running_speed = max_running_speed



