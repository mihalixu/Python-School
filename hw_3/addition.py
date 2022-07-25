"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""
def sum_to(num):
    assert num >= 0, "Input is < 0"
    sum = 0
    while num >= 0:
        sum = sum + num
        num -= 1
    return sum

