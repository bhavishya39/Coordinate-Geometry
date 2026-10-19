import math
from geometry.stline import StLine

class Circle:

    def __init__(self, h, k, r):
        self.h = h
        self.k = k
        self.r = r

    def get_equation(self):
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

    def get_circumference(self):
        if self.r >= 0:
            return 2*math.pi*self.r
        else:
            return None

    def get_area(self):
        if self.r >= 0:
            return math.pi*(self.r**2)
        else:
            return None

    def get_diameter(self):
        if self.r >= 0:
            return 2*self.r
        else:
            return None

    def get_center(self):
        return (self.h, self.k)

    def check_type(self):
        if self.r == 0:
            print("Point Circle")
        elif self.r > 0:
            print("Real Circle")
        else:
            print("Invalid")

    def get_intercepts(self):
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

    def point_position(self, x1, y1):
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

    def is_tangent(self, l):
        if self.r > 0:
            t = StLine(l[0], l[1], l[2])
            d = t.pointDistance(self.h, self.k)
            if d == self.r:
                return True
            else:
                return False
        else:
            return None

    def is_secant(self, l):
        if self.r > 0:
            t = StLine(l[0], l[1], l[2])
            d = t.pointDistance(self.h, self.k)
            if d < self.r:
                return True
            else:
                return False
        else:
            return None

    def is_external(self, l):
        if self.r > 0:
            t = StLine(l[0], l[1], l[2])
            d = t.pointDistance(self.h, self.k)
            if d > self.r:
                return True
            else:
                return False
        else:
            return None
