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

    

leo = Dog("Leo")
rex = Dog('Rex')

print(Dog.num_dogs())   #1
print(leo.num_dogs())   #2
print(rex.num_dogs())   #3 All 1-3 are the same thing
leo.bark(2)
rex.bark(3)
print(Dog.dogs)