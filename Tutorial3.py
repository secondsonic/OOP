#Inheritance

class Animal(object): #Animal is the parent
    def __init__(self,family,name,age,color): 
        self.family = family
        self.name = name    
        self.age = age
        self.color = color
        

    def speak(self):
        print('Hello! From', self.name,
              'I am a', self.family, 'and I am', self.age, 'Years old',
              'My color is', self.color)
              
    
    def bark(self):
        print(self.name, 'says: Bark!')
    
# class Cat(object):
#     def __init__(self,name,age,color): 
#         self.name = name    
#         self.age = age
#         self.color = color

#     def speak(self):
#         print('Meow Meow Meow From', self.name,
#               'And I am ', self.age, 'Years old')
#insted of copying we use "Inheritance"

class Cat(Animal): #Cat is the child
    def __init__(self, family, name, age, color, num):
        super().__init__(family, name, age, color)
        self.num = num
        print(self.name ,'Favorite number is', num)

    def bark(self): #override or overload bark method
        print(self.name, 'says: Meow!')


class Dog(Animal): #Dog is the child
    def __init__(self, family,name, age, color, numbers):
        super().__init__(family, name, age, color)
        self.numbers = numbers
        print(self.name ,'Favorite numbers are', numbers)


leo = Dog('Dog','Leo', 2, 'Black and White',[1,2,3])
yumyum = Cat('Cat','Yumyum', 1, 'Beige', 9)

leo.speak()
yumyum.speak()


leo.bark()
yumyum.bark()

#Another example of like use of Inheritance
print()

class Vehicle():
    def __init__(self, price, gas, color,horn):
        self.price = price
        self.gas = gas
        self.color = color
        self.horn = horn

    def fillUpTank(self):
        self.gas = 100
    def emptyTank(self):
        self.gas = 0
    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self, price, gas, color, horn, speed):
        super().__init__(price, gas, color, horn)
        self.speed = speed
    
    def beep(self):
        print(self.horn, 'sound: Beep Beep!')

class Truck(Vehicle):
    def __init__(self, price, gas, color, horn, tires):
        super().__init__(price, gas, color, horn)
        self.tires = tires
    
    def beep(self):
        print(self.horn, 'sound: Honk Honk!')

class SmallCar(Car): #SmallCar inherit from Car, Car inherit from Vehicle
    def __init__(self, price, gas, color, horn, speed):
        super().__init__(price, gas, color, horn, speed)

    def beep(self):
        print(self.horn, 'sound: beep!')

car = Car(100000,100,'black','Horn',220)
truck =Truck(200000,100,'red','Horn','Large')
small_car = SmallCar(10000,50,'blue','horn',120)

car.beep()
truck.beep()
small_car.beep()