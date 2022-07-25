"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""


INTEREST = float(input("Enter the fixed interest rate in percent: "))
AMOUNT_INVEST = int(input("Enter the amount of money you want to invest: "))
YEARS = int(input("Enter the number of years the money will be invested: "))

Earned_Interest = AMOUNT_INVEST * (1 + (INTEREST / 100))**YEARS

print(f"The earned interest is {round(Earned_Interest - AMOUNT_INVEST,2)}.")
print(f"The terminal value amounts to {round(Earned_Interest,2)}.")
