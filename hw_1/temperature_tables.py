"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

user_input = input("For C => F enter C, for F => C enter F: ")

celsius_starting_point = - 20
celsius_ending_point = 40

fahrenheit_starting_point = -10
fahrenheit_ending_point = 110

if user_input == 'C':
    while celsius_starting_point <= celsius_ending_point:
        print(f'{celsius_starting_point} C => {(9 / 5) * celsius_starting_point + 32:.1f} F')
        celsius_starting_point += 1
elif user_input == 'F':
    while fahrenheit_starting_point <= fahrenheit_ending_point:
        print(f'{fahrenheit_starting_point} F => {(fahrenheit_starting_point - 32 ) * 5 / 9:.1f} C')
        fahrenheit_starting_point += 1
else:
    print("sudo apt moo")
