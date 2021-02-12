#Inheritance

class Animal(object): #Animal is the parent
    def __init__(self,family,name,age,color): 
        self.name = name    
        self.age = age
        self.color = color
        self.family = family

    def speak(self):
        print('Hello! From', self.name,
              'I am a', self.family, 'and', self.age, 'Years old',
              'My color is', self.color)
              
    
    def bark(self):
        print('Bark!')
    
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
        print(name ,'Favorite number is', num)

    def bark(self): #override or overload bark method
        print('Meow!')


class Dog(Animal): #Dog is the child
    def __init__(self, family,name, age, color):
        super().__init__(family, name, age, color)


leo = Dog('Dog','Leo', 2, 'Black and White')
yumyum = Cat('Cat','Yumyum', 1, 'Beige', 9)

leo.speak()
yumyum.speak()


leo.bark()
yumyum.bark()

#Another example of like use of Inheritance
print()

class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100
    def emptyTank(self):
        self.gas = 0
    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed
    
    def beep(self):
        print('Beep Beep!')

class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
    
    def beep(self):
        print('Honk Honk!')

car = Car(10000,100,'black',365)