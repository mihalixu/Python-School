"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

import csv
num_of_closings = 0
closing_price = 0
YOURFILE = input("File to analyze: ")

with open(YOURFILE,encoding='utf-8') as f:
    for line in f:
        line = line.split(",")
        if line[4] != 'Close':
            recent_closing_price = round(float(line[4]),2)
            closing_price = closing_price + float(line[4])
            num_of_closings+=1



AVERAGE_CLOSING_PRICE = round(closing_price / num_of_closings,2)

print(f'The average closing price was {AVERAGE_CLOSING_PRICE}.')
print(f'The most recent closing price ({recent_closing_price}) was above the average.')


