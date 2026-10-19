from geometry.stline import StLine
from geometry.stline import TwoStLine
from geometry.circle import Circle

def menu():
    print(
'''
WELCOME TO THE COORDINATE GEOMETRY TOOLKIT

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
        a = float(input("Enter x coefficient: "))
        b = float(input("Enter y coefficient: "))
        c = float(input("Enter constant term: "))
        l = StLine(a, b, c)
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
                print(l.get_slope())
            elif op == "A":
                print(l.get_slope_angle())
            elif op == "e":
                l.equation()
            elif op == "i":
                l.get_intercepts()
            elif op == "d":
                p = list(map(int, input("Enter x,y coordinates of the point: ").split(",")))
                print(l.point_distance(p[0], p[1]))
            elif op == "x":
                print(l.is_xparallel())
            elif op == "y":
                print(l.is_yparallel())
            elif op == "0":
                menu()
                break
            else:
                print("Invalid Operation")
    elif curve == "1+":
        l1 = list(map(float, input("Enter coefficients and constant term of L1 in a,b,c format: ").split(",")))
        l2 = list(map(float, input("Enter coefficients and constant term of L2 in a,b,c format: ").split(",")))
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
                print(s.is_perpendicular())
            elif op == "A":
                print(s.find_angle())
            elif op == "e":
                print(s.get_equations())
            elif op == "pl":
                print(s.is_parallel())
            elif op == "d":
                print(s.line_distance())
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
                c.get_equation()
            elif op == "c":
                print(c.get_circumference())
            elif op == "a":
                print(c.get_area())
            elif op == "d":
                print(c.get_diameter())
            elif op == "z":
                print(c.get_center())
            elif op == "t":
                c.check_type()
            elif op == "i":
                c.get_intercepts()
            elif op == "p":
                p = list(map(float, input("Enter x,y coordinates of the point: ").split(",")))
                c.point_position(p[0], p[1])
            elif op == "tg":
                l = list(map(float, input("Enter coordinates and slope of line in x,y,m format: ").split(",")))
                print(c.is_tangent(l))
            elif op == "sc":
                l = list(map(float, input("Enter coordinates and slope of line in x,y,m format: ").split(",")))
                print(c.is_secant(l))
            elif op == "ex":
                l = list(map(float, input("Enter coordinates and slope of line in x,y,m format: ").split(",")))
                print(c.is_external(l))
            elif op == "0":
                menu()
                break
            else:
                print("Invalid Operation")

menu()