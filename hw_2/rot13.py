"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.com>
"""
from os import read


txt_file = input("File to decode: ")
assert txt_file == "rot13.txt", "Please Enter rot13.txt p.s rot13.txt must be in the Homework Directory!!"
print("\n")

txt = open(txt_file).read().upper()
abc_liste = []
rot13_liste = []
abc_string = ""
rot13_string = ""

for i in txt:
    if ord(i) >= 65 and ord(i) <= 77:
        abc_liste.append((chr(ord(i) + 13)))
    elif ord(i) > 77 and ord(i) <=90:
        abc_liste.append((chr(ord(i)-13)))
    else:
        abc_liste.append(chr(ord(i)))
decode = abc_string.join(abc_liste)
print(decode)



