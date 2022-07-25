"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

from math import sqrt
first_x_point = float(input("First point's x-coordinate: "))
first_y_point = float(input("First point's y-coordinate: "))

second_x_point = float(input("Second point's x-coordinate: "))
second_y_point = float(input("Second point's y-coordinate: "))

euclidean_distance = round(sqrt((second_x_point - first_x_point)**2 + (second_y_point - first_y_point)**2),4)

print(f'The euclidean distance between the two points is {euclidean_distance}.')
