"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""
from math import pi, sqrt


def perimeter_right_triangle(c1, c2):
    P =  c1 + c2 + sqrt(c1**2 + c2**2)
    return P

def area_right_triangle(c1, c2):
    A = (c1 * c2) / 2
    return A

def perimeter_circle(r):
    C = 2 * pi * r
    return C

def area_circle(r):
    A = pi * r ** 2
    return A

def surface_sphere(r):
    A = 4 * pi * r**2
    return A

def volume_sphere(r):
    V = 4 / 3 * pi * r**3
    return V

def surface_cylinder(r, h):
    A = 2 * pi * r * h + 2 * pi * r**2
    return A

def volume_cylinder(r, h):
    V = pi * r**2 * h
    return V

def surface_cone(r, h):
    A = pi * r * (r + sqrt(h**2 + r**2))
    return A

def volume_cone(r, h):
    V = pi  * r**2 * h / 3
    return V


