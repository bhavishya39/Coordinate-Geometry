import math

def findSlope(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    return (self.y2-self.y1)/(self.x2-self.x1)

class StLine:

    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

    def getSlope(self):
        return self.m

    def getSlopeAngle(self):
        return math.degrees(math.atan(self.m))
    
    def cartEquation(self):
        if self.m == 0:
            print(f"y = {self.y}")
        elif math.isnan(self.m):
            print(f"x = {self.x}")
        else:
            if self.y - self.m*self.x > 0:
                print(f"{self.m}x - y + {self.y - self.m*self.x} = 0")
            elif self.y - self.m*self.x < 0:
                print(f"{self.m}x - y - {-(self.y - self.m*self.x)} = 0")
            else:
                print(f"{self.m}x - y = 0")

    def getIntercepts(self):
        if self.m == 0:
            print(f"x intercept does not exist\ny intercept = {self.y}")
            return self.y
        elif math.isnan(self.m):
            print(f"x intercept = {self.x}\ny intercept does not exist")
            return self.x
        else:
            a = (self.m*self.x-self.y)/(self.m)
            b = self.y-self.m*self.x
            print(f"x intercept = {a}\ny intercept = {b}")
            return (a, b)
        
    def pointDistance(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        d = math.fabs(((self.m*self.x1)-(self.y1)+(self.y-self.m*self.x))/math.sqrt((self.m**2)+1))
        return d

    def isXparallel(self):
        if self.m == 0:
            return True
        else:
            return False

    def isYparallel(self):
        return math.isnan(self.m)

class TwoStLine(StLine):

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def isPerpendicular(self):
        if self.l1[2]*self.l2[2] == -1:
            return True
        else:
            return False

    def isParallel(self):
        if self.l1[2] == self.l2[2]:
            return True
        else:
            return False

    def findAngle(self):
        if self.l1[2]*self.l2[2] == -1:
            return 90
        else:
            return math.atan(math.fabs((self.l1[2]-self.l2[2])/(1+(self.l1[2]*self.l2[2]))))

    def getEquations(self):
        l1 = StLine(self.l1[0], self.l1[1], self.l1[2])
        l2 = StLine(self.l2[0], self.l2[1], self.l2[2])
        l1.cartEquation()
        l2.cartEquation()

    def lineDistance(self):
        if self.l1[2] == self.l2[2]:
            return math.fabs(((self.l1[1]-self.l1[2]*self.l1[0])-(self.l2[1]-self.l2[2]*self.l2[0]))/(math.sqrt((self.l1[2]**2)+1)))
        else:
            return 0

    def solve(self):
        if self.l1[2] == self.l2[2]:
            print("No solution")
        else:
            x = ((self.l2[2]*self.l2[0]-self.l1[2]*self.l1[0])+(self.l1[1]-self.l2[1]))/(self.l2[2]-self.l1[2])
            y = (self.l1[2]*self.l2[2]*(self.l2[0]-self.l1[0])+(self.l2[2]*self.l1[1]-self.l1[2]*self.l2[1]))/(self.l2[2]-self.l1[2])
            return (x, y)

class Circle:

    def __init__(self, h, k, r):
        self.h = h
        self.k = k
        self.r = r

    def getEquation(self):
        if self.r >= 0:
            if self.h == 0 and self.k == 0:
                print(f"x^2 + y^2 = {self.r**2}")
            elif self.h == 0 and self.k > 0:
                print(f"x^2 + (y - {self.k})^2 = {self.r**2}")
            elif self.h == 0 and self.k < 0:
                print(f"x^2 + (y + {math.fabs(self.k)})^2 = {self.r**2}")
            elif self.h > 0 and self.k == 0:
                print(f"(x - {self.h})^2 + y^2 = {self.r**2}")
            elif self.h < 0 and self.k == 0:
                print(f"(x + {math.fabs(self.h)})^2 + y^2 = {self.r**2}")
            elif self.h > 0 and self.k > 0:
                print(f"(x - {self.h})^2 + (y - {self.k})^2 = {self.r**2}")
            elif self.h > 0 and self.k < 0:
                print(f"(x - {self.h})^2 + (y + {math.fabs(self.k)})^2 = {self.r**2}")
            elif self.h < 0 and self.k > 0:
                print(f"(x + {math.fabs(self.h)})^2 + (y - {self.k})^2 = {self.r**2}")
            elif self.h < 0 and self.k < 0:
                print(f"(x + {math.fabs(self.h)})^2 + (y + {math.fabs(self.k)})^2 = {self.r**2}")
        else:
            print("Invalid")

    def getCircumference(self):
        if self.r >= 0:
            return 2*math.pi*self.r
        else:
            print("Invalid")

    def getArea(self):
        if self.r >= 0:
            return math.pi*(self.r**2)
        else:
            print("Invalid")

    def getDiameter(self):
        if self.r >= 0:
            return 2*self.r
        else:
            print("Invalid")

    def getCenter(self):
        return (self.h, self.k)

    def checkType(self):
        if self.r == 0:
            print("Point Circle")
        elif self.r > 0:
            print("Real Circle")
        else:
            print("Invalid")

    
    def getIntercepts(self):
        if self.r > 0:
            g = -self.h
            f = -self.k
            c = (self.h**2)+(self.k**2)-(self.r**2)
            x = (g**2) - c
            y = (f**2) - c
            if x < 0 and y < 0:
                print("No Intercepts")
            elif x == 0 and y == 0:
                print(f"Circles touches both the axes at ({self.r}, 0) and (0, {self.r}), and has intercepts equal to 0")
            elif x == 0 and y < 0:
                print(f"X intercept = 0\nY intercept does not exist")
            elif x == 0 and y > 0:
                print(f"X intercept = 0\nY intercept = {2*math.sqrt(y)}")
            elif x > 0 and y == 0:
                print(f"X intercept = {2*math.sqrt(x)}\nY intercept = 0")
            elif x < 0 and y == 0:
                print(f"X intercept does not exist\nY intercept = 0")
            elif x > 0 and y > 0:
                print(f"X intercept = {2*math.sqrt(x)}\nY intercept = {2*math.sqrt(y)}")
        else:
            print("Invalid")

    def pointPosition(self, x1, y1):
        if self.r > 0:
            self.x1 = x1
            self.y1 = y1
            s = ((self.x1-self.h)**2) + ((self.y1-self.k)**2) - (self.r**2)
            if s < 0:
                print("Point lies inside the circle")
            elif s == 0:
                print("Point lies on the circle")
            else:
                print("Point lies outside the circle")
        else:
            print("Invalid")

    def isTangent(self, l):
        if self.r > 0:
            t = StLine(l[0], l[1], l[2])
            d = t.pointDistance(self.h, self.k)
            if d == self.r:
                return True
            else:
                return False
        else:
            print("Invalid")

    def isSecant(self, l):
        if self.r > 0:
            t = StLine(l[0], l[1], l[2])
            d = t.pointDistance(self.h, self.k)
            if d < self.r:
                return True
            else:
                return False
        else:
            print("Invalid")

    def isExternal(self, l):
        if self.r > 0:
            t = StLine(l[0], l[1], l[2])
            d = t.pointDistance(self.h, self.k)
            if d > self.r:
                return True
            else:
                return False
        else:
            print("Invalid")

    
    