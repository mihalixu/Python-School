"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

def encode(string:str):
    
    abc_list = []
    abc_string = ""

    for char in string.upper():
        if ord(char) >= 65 and ord(char) <= 77:
            abc_list.append((chr(ord(char) + 13)))
        elif ord(char) > 77 and ord(char) <=90:
            abc_list.append((chr(ord(char)-13)))
        else:
            abc_list.append(chr(ord(char)))
    
    encode = abc_string.join(abc_list)
    return encode

#No need for decode(.) function because encode is both encode and decode function
def decode(string:str):
    
    abc_list = []
    abc_string = ""

    for char in string.upper():
        if ord(char) >= 65 and ord(char) <= 77:
            abc_list.append((chr(ord(char) + 13)))
        elif ord(char) > 77 and ord(char) <=90:
            abc_list.append((chr(ord(char)-13)))
        else:
            abc_list.append(chr(ord(char)))
    
    decode = abc_string.join(abc_list)
    return decode



