import math

class Vector2(object):
    
    def __init__(self, x=0, y=0):        
        self.x = x
        self.y = y

        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]
        
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
        
    def from_points(P1, P2):        
        return Vector2( P2[0] - P1[0], P2[1] - P1[1] )
    
    def get_magnitude(self):        
        return math.sqrt( self.x**2 + self.y**2 )
        
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
        
    @property
    def value(self):
        return (self.x, self.y)
        
    def __add__(self, rhs):         
        return Vector2(self.x + rhs.x, self.y + rhs.y)
        
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
        
    def __neg__(self):
        return Vector2(-self.x, -self.y)
        
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
        
    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = 1.0 * value
