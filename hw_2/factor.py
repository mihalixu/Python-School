"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

Number = int(input("Integer: "))

factor = 2
sum = 1
limit = Number
list_of_factors = []
result_list = [Number,"=",]


while sum < limit:
    if Number % factor == 0:
        Number = Number / factor
        sum = sum * factor
        list_of_factors.append(factor)
    else:
        factor+=1



for index,element in enumerate(list_of_factors):
    if index == len(list_of_factors) - 1:
        result_list.append(element)
    else:
        result_list.append(element)
        result_list.append("*")

for element in result_list:
    print(element, end=" ")


