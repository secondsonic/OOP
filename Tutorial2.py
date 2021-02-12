#Creating Classes
#Methods look just like funcs, but you have to call them using an object. 
class Dog(object):
    def __init__(self,name,age): #Constructor or initialization Method, self is an attribute.
        self.name = name    #self represnts the instance
        self.age = age
        self.fav_numbers = [1,3,5]
        
    
    def speak(self):
        print('Bark Bark Bark From', self.name,
              'And I am ', self.age, 'Years old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


"""
You do not need to od like leo.__init__()
when you call the class such as Dog()
the __init__ will automatically happen
"""
#leo -> self so leo.name -> Leo and leo.age -> 2
leo = Dog('Leo',2) #leo is an instance of type or class dog
#rex -> self so rex.name -> Rex and rex.age -> 3
rex = Dog('Rex',3)
leo.change_age(4)

leo.speak()
rex.speak()
#lets say I wanna just access Rex's age
print(rex.age)
print(leo.fav_numbers)

leo.add_weight(80)
rex.add_weight(70)
print(leo.weight)
print(rex.weight)

