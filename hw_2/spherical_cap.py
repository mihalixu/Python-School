"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""



from math import pi

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))


Area = (2 * pi * radius * height)
Volume = ((pi * height**2) / 3) * (3 * radius - height) 

print(f'The spherical cap has a surface of {Area:.3f}')
print(f'The volume of the spherical cap is {Volume:.3f}')
