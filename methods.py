class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'

    def add(self, v):
        if type(v) == Vec2:
            return Vec2(self.x + v.x, self.y + v.y)
        else:
            raise TypeError('Argument must be a Vec2 object.')

    def sub(self, v):
        if type(v) == Vec2:
            return Vec2(self.x - v.x, self.y - v.y)
        else:
            raise TypeError('Argument must be a Vec2 object.')

    def mult(self, n):
        if type(n) == int or type(n) == float:
            return (self.x * n, self.y * n)
        else:
            raise TypeError('Argument must be an int or a float.')

x = Vec2(3, 5)
y = Vec2(2, 9)
z = 4
print(x.sub(y))
print(y.mult(z))
print(y.add(x))
print(x.add(z))