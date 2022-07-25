"""
.. moduleauthor:: Your Name <mihael.subasic@bulme.at>
"""

from math import pi

radius = int(input("Enter a radius: "))

volume = round((4 / 3) * pi * radius**3,2)
area = round(4 * pi * radius**2,2)

print(f"The sphere has a volume of {volume} ")
print(f"The surface area of this sphere is {area}")
