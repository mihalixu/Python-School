#!/usr/bin/env python3

from grader import grade_by_io

task1 = "spherical_cap.py"
input1 = "3.4\n2.1\n"
expected1 = ("Enter the radius: "
             "Enter the height: "
             "The spherical cap has a surface of 44.862\n"
             "The volume of the spherical cap is 37.407\n")

task2 = "quadratic_equation.py"
input2 = "2.7\n-4.3\n5.5\n"
expected2 = ("a: "
             "b: "
             "c: "
             "x1: 0.80+1.18j x2: 0.80-1.18j\n")

task3 = "even.py"
input3 = "48\n"
expected3 = ("Upper limit: "
             "0\n4\n16\n36\n")

task4 = "special_sum.py"
input4 = "7\n63\n"
expected4 = ("Denominator: "
             "Upper limit: "
             "Sum: 315\n")

task5 = "search.py"
input5 = "f1.txt,f2.txt\nlorem\n"
expected5 = ("Files: "
             "Needle: "
             "Occurrences: 12\n")

task6 = "downloading.py"
input6 = ""
expected6 = "Next weekend, hiking would be a good activity.\n"

task7 = "print_demand.py"
input7 = ""
expected7 = "Total demand: 1458.0\n"

task8 = "financial_data.py"
input8 = "ANDR.VI.csv\n"
expected8 = "File to analyze: "
# expected value needs to be calculated
CLOSING_PRICE_COL = 4
try:
    with open(input8.strip()) as f:
        f.readline()
        current_closing = float(f.readline().split(',')[CLOSING_PRICE_COL])
        average_closing = current_closing
        value_count = 1
        for line in f:
            if not line.strip():
                continue
            current_closing = float(line.split(',')[CLOSING_PRICE_COL])
            average_closing += current_closing
            value_count += 1
    average_closing /= value_count
    expected8 += ("The average closing price was {:.2f}.\n"
                  .format(average_closing))
    if current_closing > average_closing:
        expected8 += ("The most recent closing price ({}) was above the "
                      "average.\n".format(current_closing))
    else:
        expected8 += ("The most recent closing price ({}) was not above the "
                      "average.\n".format(current_closing))
    grade_task8 = True
except FileNotFoundError:
    print('Grader misses Andritz AG\'s stock data ({}). Skipping task.'
          .format(input8.strip()))
    grade_task8 = False

task9 = "factor.py"
input9 = "63"
expected9 = ("Integer: "
             "63 = 3 * 3 * 7\n")

task10 = "rot13.py"
input10 = "rot13.txt\n"
expected10 = ("File to decode: "
              "APT-GET MOO\n"
              "APT-BUILD MOO\n\n")


total = 0
total += grade_by_io(task1, input1, expected1, 0.5)
total += grade_by_io(task2, input2, expected2)
total += grade_by_io(task3, input3, expected3, 0.5)
total += grade_by_io(task4, input4, expected4)
total += grade_by_io(task5, input5, expected5)
total += grade_by_io(task6, input6, expected6)
total += grade_by_io(task7, input7, expected7)
if grade_task8:
    total += grade_by_io(task8, input8, expected8)
total += grade_by_io(task9, input9, expected9)
total += grade_by_io(task10, input10, expected10)

print()
print(total, "in total")
print('KDE Rocks :)')

