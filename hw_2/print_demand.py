"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

import requests

url = "https://bulme.find-santa.eu/data/python/r101.txt"

r = requests.get(url, allow_redirects=True)
demand = 0
open("demand.txt","wb").write(r.content)

with open("demand.txt", encoding="utf-8") as f:
    for line in f:
        line = line.split()
        if line[3] != 'DEMAND':
            demand = demand + float(line[3])
    

print(f"Total demand: {demand}\n")
