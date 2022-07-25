"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""



denominator = int(input("Denominator: "))
uper_limit = int(input("Upper limit: "))

starting_num = 1
sum = 0

while starting_num <= uper_limit:
    if starting_num % denominator == 0:
        sum = sum + starting_num
    starting_num +=1

print(f'Sum: {sum}')

