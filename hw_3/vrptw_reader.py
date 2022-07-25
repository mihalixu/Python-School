"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

from math import sqrt

def read_string_list(filename="r101"):
    txt_list = []
    txt_counter = 0

    for txt in filename:
        if txt == '.' or txt == 't' or txt == 'x':
            txt_counter +=1

    if txt_counter < 4:
        filename = filename + '.txt'

    with open(filename,encoding='utf-8') as f:
        for line in f:
            txt_list.append(line)
        return txt_list[1:]




def get_demand(list,CUST_NO):
    assert CUST_NO <= 101 ,"Custom_NO is to high"
    for element in list:
        element = str(element).split()
        if str(CUST_NO) == element[0]:
            return float(element[3])




def calc_distance(list,FIRST_CUST_NO,SECOND_CUST_NO):
    
    assert FIRST_CUST_NO <= 101 ,"FIRST_CUST_NO is to high"
    assert SECOND_CUST_NO <= 101 ,"SECOND_CUST_NO is to high"

    for element in list:
        element = str(element).split()
        if str(FIRST_CUST_NO) == element[0]:
            x1 = float(element[1]) 
            y1 = float(element[2])
        if str(SECOND_CUST_NO) == element[0]:
            x2 = float(element[1])
            y2 = float(element[2])
    return sqrt((x1-x2)**2 + (y1-y2)**2)
    
