#Static Methods and Class Methods

class Dog():
    dogs = []   #better to put statically used vars inside the class
    
    def __init__(self,name):
        self.name = name
        self.dogs.append(self.name)


    @classmethod    #this is a decorator
    def num_dogs(cls):  #the cls is always cls or class
        return len(cls.dogs)

    @staticmethod   #statics are the functions you want to use
    def bark(n):
        #barks n times
        for _ in range(n):
            print('Bark!')
    def __str__(self):
        return str(self.dogs)

    

leo = Dog("Leo")
rex = Dog('Rex')

print(Dog.num_dogs())
print(leo.num_dogs())
print(rex.num_dogs())
leo.bark(2)
rex.bark(3)
print(Dog.dogs)