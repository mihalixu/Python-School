"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""
def interest(capital, rate, years=1, tax=0):
    if tax > 0:
        Zinszins_tax = capital * (rate - (rate * tax) + 1)**years - capital
        return Zinszins_tax
    else:
        Endwert = capital * (1 + rate)**years
        Zinsenzins = Endwert - capital
        return Zinsenzins

def terminal_value(capital, rate, years=1, tax=0):

    if tax > 0:
        Endwert_tax = capital * (rate - (rate * tax) + 1)**years
        return Endwert_tax
    else:
        Endwert = capital * (1 + rate)**years
        return Endwert




