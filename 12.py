
class My_time:
    def __init__(self,hours,minute,seconds):
        self.hours = hours
        self.minute = minute
        self.seconds = seconds

    

    

    def __add__(self,other):
        return My_time(self.hours + other.hours,self.minute + other.minute, self.second + other.secods)


    def __sub__(self,other):
        while self.seconds > 60:
            self.seconds = self.seconds - 60
            self.minutes += 1
        while self.minutes > 60:
            self.minutes = self.minutes - 60
            self.hours += 1
        while other.seconds > 60:
            self.seconds = other.seconds - 60
            self.minutes += 1
        while other.minutes > 60:
            self.minutes = other.minutes - 60
            self.hours += 1
    
    
        return My_time(self.hours - other.hours,self.minute - other.minute, self.second - other.secods)

first = My_time(0,1,0)
second = My_time(0,0,60)
print(first == second)

