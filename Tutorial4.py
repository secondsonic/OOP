#Overriding Methods

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.cords = (self.x, self.y)
        print(self.cords)
    
    def move(self, x, y):
        self.x += x
        self.y += y
        print(self.cords, 'Moves to:', self)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __len__(self): #or a func call it lenght or whatever can be use read about it
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.__len__() > p.__len__()
    
    def __ge__(self, p):
        return self.__len__() >= p.__len__()
    
    def __lt__(self, p):
        return self.__len__() < p.__len__()

    def __le__(self, p):
        return self.__len__() <= p.__len__()
        
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)
p8 = Point(3,4)

print()

p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

print(p7)

p2.move(1,2)
p4.move(1,0)
newp5 = p1 + p2
newp6 = p4 - p1
# print(p5, p6, p7)
print(p1 == p2)
print(p1 == p8)

