"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

"""
This functions takes text as input and gives numbers as output
Hint: not for every Char.
"""


def as_numeric(text):
    return_list = []
    upper_text = str(text).upper()

    for s in upper_text:
        if (ord(s) >= 65 and ord(s) <=67):
            return_list.append('2')
        elif (ord(s) >= 68 and ord(s) <=70):
            return_list.append('3')
        elif (ord(s) >= 71 and ord(s) <=73):
            return_list.append('4')
        elif (ord(s) >= 74 and ord(s) <=76):
            return_list.append('5')
        elif (ord(s) >= 77 and ord(s) <=79):
            return_list.append('6')
        elif (ord(s) >= 80 and ord(s) <=83):
            return_list.append('7')
        elif (ord(s) >= 84 and ord(s) <=86):
            return_list.append('8')
        elif (ord(s) >= 87 and ord(s) <=90):
            return_list.append('9')
        else:
            return_list.append(s)
    result = ''.join(return_list)
    return str(result)

