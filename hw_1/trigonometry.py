"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

from math import pi, sin, tan

starting_number = - 0.1

print("radians |  sine | tangent ")
print("-------------------------")
while pi > starting_number:
    starting_number += 0.1
    if starting_number > pi:
        starting_number = pi
    rad = round(starting_number,2)
    sine = round(sin(starting_number),2)
    tangent = round(tan(starting_number),2)
    print(f'   {rad:>4} |  {sine:>4} |   {tangent:>5}')




