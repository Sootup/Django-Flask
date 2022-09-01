class Car:
    def __init__(self,mark,model,year,speed):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed


    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self,mark):
        self.__mark = mark
        
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self,model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,year):
        self.__year = year
    
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self,speed):
        self.__speed = speed

 
    def speed_increase(self,speed = 5):
        if speed:
            self.__speed += speed
            return self.__speed
        else:
            return self.__speed

    def speed_decrease(self,speed = speed ):
        if speed:
            self.__speed -= 5
            return self.__speed
        else:
            return self.__speed


    def stop(self,speed = 0):
        self.__speed = speed
        print(speed)


    def show_speed(self):
        print(self.__speed)
    
        

    def turn(self):
        print(-self.__speed)


car1 = Car("mazda",'zx',2010,0)

car1.speed_increase()
car1.speed_decrease()
car1.speed_increase()
car1.speed_increase()
car1.speed_increase()
car1.speed_increase()
car1.show_speed()
car1.turn()
car1.stop()