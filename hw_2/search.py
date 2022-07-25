"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""


user_input = input("Files: ").split(",")
needle = input("Needle: ").upper()
ocurrences = 0


for indx in user_input:
    with open (indx,encoding="utf-8") as f:
        for line in f:
            line = line.upper().split()
            for str in line:
                if str == needle:
                    ocurrences+=1
            

print(f'Occurrences: {ocurrences}')
