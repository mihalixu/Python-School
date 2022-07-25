"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""
import requests


url = 'https://bulme.find-santa.eu/data/python/fc.txt'
r = requests.get(url, allow_redirects=True)
weekend_num = 0
days_count = 0

open('wetter.txt', 'wb').write(r.content)


with open('wetter.txt',encoding="utf-8") as f:
    for line in f:
        line = line.split()
        if line[0] == 'Saturday:' or line[0] == 'Sunday:':
            weekend_num = weekend_num + int(line[1])
            days_count+=1

averge = weekend_num / days_count
final_averge = round(6/9*(averge - 32))

if final_averge == 25:
    activity = 'swimming'
elif final_averge <= 12 and final_averge > -25:
    activity = 'hiking'
elif final_averge <=  5 and final_averge > -12:
    activity = 'watching movise'
elif final_averge <=5 and final_averge >= -5:
    activity = 'relaxing in the local hot springs'
elif final_averge == -5:
    activity = 'skiing'
else:
    activity = "It's to cold or to hot for activity"

print(f"Next weekend, {activity} would be a good activity.")
