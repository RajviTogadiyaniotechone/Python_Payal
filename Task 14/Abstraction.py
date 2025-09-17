# Abstarction is a concept of to hide irrelavant data from the user 
# only that part of the data is tobe shown what is relavant to the user

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        @abstractmethod
        def printdetails(self):
            pass

        def accelerate(self):
            print("Speed up")

        def break_apply(self):
            print("Break applied")

        class Hatchbreak(Car):
            def printdetails(self):
                print("Brand:",self.brand)
                print("Model:",self.model)
                print("Year:",self.year)

            def sunroof():
                print("Not Avilable")

        car1 = Hatchbreak("Maruti", 1985, 2568)

        car1.printdetails()
        car1.sunroof()
        car1.brand()