# 1.
# lets design a 2d vector class set

# Think about what data the class will hold
# x, y coord

# Think about what methods it needs
# init, str

# Think about what methods could be optional
# add, subtract, 

# Draw out diagrams of the class model
"""
 |------------|  
 | x, y       |    <- fields
 |------------|
 |  __str__   |    <- base methods
 | __init__   |
 |------------|
 |    add     |   <- optional
 |    sub     |
 |    mul     |
 |------------|
 
 V = Vec2(20, 10)
 V2 = Vec(10, 10)
 V.add(V2) ? overload + operator 
 V += V2 
 V3 = V + V2
"""

# visualize how it will be formed

# write out a basic structure

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __str__(self):
        return "Vec2(x = %d, y = %d)" % (self.x, self.y)
    
    def add(self, other):
        self.x += other.x 
        self.y += other.y 
        
        
    #overload + opartor
    def __add__(self, other):
        ret = Vec2(self.x, self.y)
        ret.x = self.x + other.x 
        ret.y = self.y + other.y
        return ret
    
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y 
        
    def mul(self, other):
        self.x *= other.x
        self.y *= other.y
        
    def divide(self, other):
        self.x /= other.x
        self.y /= other.y 
        
    def idiv(self, other):
        self.x //= other.x
        self.y //= other.y 


v1 = Vec2(20, 10)
v2 = Vec2(10, 10)

print('--------------------')
print(v1)
print(v2)
print('--------------------')
v1.add(v2)
print(v1)
print(v2)
print('--------------------')
v1.sub(v2)
print(v1)
print(v2)
print('--------------------')
v1.mul(v2)
print(v1)
print(v2)
print('--------------------')
v1.divide(v2)
print(v1)
print(v2)
print('--------------------')
v3 = v1 + v2 
print(v1)
print(v2)
print(v3)
print('--------------------')

# 2.
# Linked Lists to trees
"""
Singly linked list
(value) -> (value) ->()

Doubly linked list
<- (value) <--> (value) <-->()->

Tree from DLL
        (value)
        /     \ 
    (left)    (right)
"""