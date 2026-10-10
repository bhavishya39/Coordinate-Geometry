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
            return f"y = {self.y}"
        elif math.isnan(self.m):
            return f"x = {self.x}"
        else:
            if self.y - self.m*self.x > 0:
                return f"{self.m}x - y + {self.y - self.m*self.x} = 0"
            elif self.y - self.m*self.x < 0:
                return f"{self.m}x - y - {-(self.y - self.m*self.x)} = 0"
            else:
                return f"{self.m}x - y = 0"

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
        print(l1.cartEquation())
        print(l2.cartEquation())

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

