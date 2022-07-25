"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

user_input = float(input("Enter a temperature in degrees Fahrenheit: "))

convert = round((5 / 9) * (user_input - 32),2)
print(f"72.3 degrees Fahrenheit correspond to {convert} degrees Celsius")
