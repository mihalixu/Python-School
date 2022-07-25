"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""
limit = int(input("Upper limit: "))

starting_num = 0


while True:
    squere_num = starting_num*starting_num
    if starting_num % 2 == 0:
        print(squere_num)
    if squere_num > limit:
        break
    starting_num +=1
