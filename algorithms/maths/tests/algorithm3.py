# This algorithm finds the square roots of an equation of the form ax^2 + bx + c = 0

import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = b * b - 4 * a * c   # determinant

if d >= 0:
    if d == 0:
        x = -b / 2 * a
        print(x)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(x1, x2)
else:
    print("no roots")


