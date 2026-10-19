import math

class StLine:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_slope(self):
        try:
            return (-self.a/self.b)
        except ZeroDivisionError:
            return math.nan

    def get_slope_angle(self):
        if self.b == 0:
            return 90
        else:
            return math.degrees(math.atan(self.get_slope()))

    def equation(self):
        if self.a == 0:
            print(f"y = {-self.c/self.b}")
        elif self.b == 0:
            print(f"x = {-self.c/self.a}")
        elif self.a == 0 and self.b == 0:
            print("Invalid line")
        elif self.c == 0:
            print(f"y = {(-self.a/self.b)}x")
        else:
            if self.c < 0:
                print(f"y = {(-self.a/self.b)}x + {(-self.c/self.b)}")
            elif self.c > 0:
                print(f"y = {(-self.a/self.b)}x - {(self.c/self.b)}")

    def get_intercepts(self):
        if self.a == 0:
            print(f"x intercept does not exist\ny intercept = {-self.c/self.b}")
        elif self.b == 0:
            print(f"x intercept = {-self.c/self.a}\ny intercept does not exist")
        else:
            a = (-self.c/self.a)
            b = (-self.c/self.b)
            print(f"x intercept = {a}\ny intercept = {b}")
        
    def point_distance(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        d = math.fabs(((self.a*self.x1)+(self.b*self.y1)+self.c)/(math.sqrt((self.a**2)+(self.b**2))))
        return d

    def is_xparallel(self):
        if self.a == 0:
            return True
        else:
            return False

    def is_yparallel(self):
        if self.b == 0:
            return True
        else:
            return False

class TwoStLine:

    def __init__(self, l1, l2):
        # l1 and l2 are lists of form [a, b, c] representing the line equation ax + by + c = 0
        self.l1 = l1
        self.l2 = l2
        self.m1 = (-self.l1[0]/self.l1[1]) if self.l1[1] != 0 else math.nan
        self.m2 = (-self.l2[0]/self.l2[1]) if self.l2[1] != 0 else math.nan


    def is_perpendicular(self):
        if self.m1*self.m2 == -1:
            return True
        else:
            return False

    def is_parallel(self):
        if self.m1 == self.m2:
            return True
        else:
            return False

    def find_angle(self):
        if self.m1*self.m2 == -1:
            return 90
        else:
            return math.degrees(math.atan(math.fabs((self.m1-self.m2)/(1+(self.m1*self.m2)))))

    def get_equations(self):
        l1 = StLine(self.l1[0], self.l1[1], self.l1[2])
        l2 = StLine(self.l2[0], self.l2[1], self.l2[2])
        l1.equation()
        l2.equation()

    def line_distance(self):
        if self.m1 == self.m2:
            d = math.fabs(((self.l1[2]*self.l2[0])-(self.l2[2]*self.l1[0]))/(math.sqrt(((self.l1[0]*self.l2[0])**2)+((self.l1[1]*self.l2[1])**2))))
            return d
        else:
            return 0

    def solve(self):
        if self.m1 == self.m2:
            return None
        else:
            x = (
                ((self.l2[2]*self.l1[1])-(self.l1[2]*self.l2[1]))/((self.l1[0]*self.l2[1])-(self.l2[0]*self.l1[1]))
            )
            y = (
                ((self.l2[2]*self.l1[0])-(self.l1[2]*self.l2[0]))/((self.l1[1]*self.l2[0])-(self.l2[1]*self.l1[0]))
            )
            return (x, y)
