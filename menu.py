from main import StLine
from main import TwoStLine
from main import Circle

def menu():
    print(
'''
WELCOME TO COORDINATE GEOMETRY FRAMEWORK

Enter 1 for Single Straight Line
Enter 1+ for Two Straight Lines
Enter 2 for Circle
Enter 3 for Parabola
Enter 4 for Ellipse
Enter 5 for Hyperbola
'''
    )
    curve = input()
    if curve == "1":
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        m = float(input("Enter slope: "))
        l = StLine(x, y, m)
        print(
'''
Single Straight Line operations:
m to get the slope
A to get slope angle
e to get equation of line
i to get intercepts
d to get perpendicular distance from a point
x to check if line parallel to x axis
y to check if line parallel to y axis
0 to exit Straight Line mode
'''
        )
        while True:
            op = input("Enter operation: ")
            if op == "m":
                print(l.getSlope())
            elif op == "A":
                print(l.getSlopeAngle())
            elif op == "e":
                print(l.cartEquation())
            elif op == "i":
                print(l.getIntercepts())
            elif op == "d":
                p = list(map(int, input("Enter x,y coordinates of the point: ").split(",")))
                print(l.pointDistance(p[0], p[1]))
            elif op == "x":
                print(l.isXparallel())
            elif op == "y":
                print(l.isYparallel())
            elif op == "0":
                menu()
                break
            else:
                print("Invalid Operation")
    elif curve == "1+":
        l1 = list(map(float, input("Enter coordinates and slope of line one in x,y,m format: ").split(",")))
        l2 = list(map(float, input("Enter coordinates and slope of line two in x,y,m format: ").split(",")))
        s = TwoStLine(l1, l2)
        print(
'''
Two Straight Lines operations:
pd to check if perpendicular
pl to check if parallel
e to get equation of lines
A to get angle between them
d to get distance between them
s to solve the equations
0 to exit Two Straight Lines mode
'''
        )
        while True:
            op = input("Enter operation: ")
            if op == "pd":
                print(s.isPerpendicular())
            elif op == "A":
                print(s.findAngle())
            elif op == "e":
                print(s.getEquations())
            elif op == "pl":
                print(s.isParallel())
            elif op == "d":
                print(s.lineDistance())
            elif op == "s":
                print(s.solve())
            elif op == "0":
                menu()
                break
            else:
                print("Invalid Operation")
    elif curve == "2":
        x = float(input("Enter x coordinate of center: "))
        y = float(input("Enter y coordinate of center: "))
        r = float(input("Enter radius: "))
        c = Circle(x, y, r)
        print(
'''
Circle operations:
e to get equation of circle
c to get circumference
a to get area
d to get diameter
z to get center
t to check type
i to get intercepts
p to check position of a point with respect to circle
tg to check if line is tangent
sc to check if line is secant
ex to check if line is external
0 to exit Circle mode
'''
        )
        while True:
            op = input("Enter operation: ")
            if op == "e":
                print(c.getEquation())
            elif op == "c":
                print(c.getCircumference())
            elif op == "a":
                print(c.getArea())
            elif op == "d":
                print(c.getDiameter())
            elif op == "z":
                print(c.getCenter())
            elif op == "t":
                print(c.checkType())
            elif op == "i":
                print(c.getIntercepts())
            elif op == "p":
                p = list(map(float, input("Enter x,y coordinates of the point: ").split(",")))
                print(c.pointPosition(p[0], p[1]))
            elif op == "tg":
                l = list(map(float, input("Enter coordinates and slope of line in x,y,m format: ").split(",")))
                print(c.isTangent(l))
            elif op == "sc":
                l = list(map(float, input("Enter coordinates and slope of line in x,y,m format: ").split(",")))
                print(c.isSecant(l))
            elif op == "ex":
                l = list(map(float, input("Enter coordinates and slope of line in x,y,m format: ").split(",")))
                print(c.isExternal(l))
            elif op == "0":
                menu()
                break
            else:
                print("Invalid Operation")

menu()