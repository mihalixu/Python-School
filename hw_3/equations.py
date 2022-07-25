"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""
from cmath import sqrt


def quadratic(a, b, c):
    b = b * -1
    q = b ** 2 - 4 * a * c
    x1 = (b + sqrt(q)) / (2 * a)
    x2 = (b - sqrt(q)) / (2 * a)
    return x1,x2




