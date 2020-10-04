class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'

    def add(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def sub(self, v):
        return Vec2(self.x - v.x, self.y - v.y)

    def mult(self, n):
        return (self.x * n, self.y * n)