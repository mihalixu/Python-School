"""
.. moduleauthor:: Your Name <mihael.subasic@bulme.at>
"""

Celsius = -15

while Celsius <= 35:
    fConvert = round((9 / 5) * Celsius + 32,2)
    print(f"{Celsius} C => {fConvert} F")
    Celsius+=1

