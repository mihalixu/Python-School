"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""


user_input = float(input("Enter a distance in meters: "))

inches_to_metar = 0.0254

print(f"{user_input / inches_to_metar:.2f} inch")
print(f"{user_input / (inches_to_metar * 12):.2f} feet")
print(f"{user_input / (inches_to_metar * 36):.2f} yards")
print(f"{user_input / (inches_to_metar * 36 * 1760):.2f} miles")

