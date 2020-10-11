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
            raise TypeError

    def sub(self, v):
        if type(v) == Vec2:
            return Vec2(self.x - v.x, self.y - v.y)
        else:
            raise TypeError

    def mult(self, n):
        if type(n) == int or type(n) == float:
            return (self.x * n, self.y * n)
        else:
            raise TypeError

x = Vec2(3, 5)
y = Vec2(2, 9)
print(x.sub(y))
print(y.mult(3))
print(y.add(x))