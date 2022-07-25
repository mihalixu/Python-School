"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

from cmath import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

b = b * -1

q = sqrt(b**2 - 4 * a * c)
x1 = (b + q) / (2 * a)
x2 = (b - q) / (2 * a)
print(f'x1: {x1:.2f} x2: {x2:.2f}')

