# Class can be defined as the collection of the objects. 
# It is an logical entity that has some attribute and methods
# class can be defined by the class keyword.

class car:
    def __init__(self, brand, year, name):
        self.brand = brand
        self.year = year
        self.name = name

    def display(self):
        print(f"{self.brand}, {self.year}, {self.name}")

my_car = car("Audi", 2024, "ab")
my_car.display()

class Electric_car(car):
    def __init__(self, brand, year, name, battery_size):
        super().__init__(brand, year, name)
        self.battery_size = battery_size

    def display_battery(self):
        print(f"battery size of the car is {self.battery_size} kwh")
        
my_electric_car = Electric_car("Tesla", 2022, "Model S", 100)
my_electric_car.display_battery()
my_electric_car.display()

print("\n")
print("-----------------------------")
# Encaptulation is refers to the bunding of the classes and attributes in the single class.

class computer:
    def __init__(self):
        self.maxprice = 700

    def sell(self):
        print("Selling price of the computer is {}".format(self.maxprice))

    def SetMaxPrice(self, price):
        self.maxprice = price

c = computer()
c.sell()

# change the price
c.maxprice = 1000
c.sell()

# using setter function
c.SetMaxPrice(77)
c.sell()

print("\n")
print("-----------------------------")

# Inheritance refers to the concept that a child class to inherit the properties and attributes of the parent class.

class Animal():
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
#Dog.speak()

print("\n")
print("-----------------------------")

# Polymorphisam refers to the one name many forms poly means 'one' and morphisam means 'many forms'

class cat(Animal):
    def speak(self):
        print("Cat speaks")

animals = [Dog(), cat()]

for a in animals:
    a.speak()

