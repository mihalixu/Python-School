#!/usr/bin/env python3

from grader import grade_by_io

task1 = "simplemath.py"
input1 = ""
expected1 = "26\n"

task2 = "fahrenheit_to_celsius.py"
input2 = "72.3\n"
expected2 = ("Enter a temperature in degrees Fahrenheit: "
             "72.3 degrees Fahrenheit correspond to 22.39 degrees Celsius\n")

task3 = "interest.py"
input3 = "3.2\n3000\n5\n"
expected3 = ("Enter the fixed interest rate in percent: "
             "Enter the amount of money you want to invest: "
             "Enter the number of years the money will be invested: "
             "The earned interest is 511.72.\n"
             "The terminal value amounts to 3511.72.\n")

task4 = "sphere.py"
input4 = "2\n"
expected4 = ("Enter a radius: "
             "The sphere has a volume of 33.51\n"
             "The surface area of this sphere is 50.27\n")

task5 = "celsius_to_fahrenheit.py"
input5 = ""
expected5 = """-15 C => 5.0 F
-14 C => 6.8 F
-13 C => 8.6 F
-12 C => 10.4 F
-11 C => 12.2 F
-10 C => 14.0 F
-9 C => 15.8 F
-8 C => 17.6 F
-7 C => 19.4 F
-6 C => 21.2 F
-5 C => 23.0 F
-4 C => 24.8 F
-3 C => 26.6 F
-2 C => 28.4 F
-1 C => 30.2 F
0 C => 32.0 F
1 C => 33.8 F
2 C => 35.6 F
3 C => 37.4 F
4 C => 39.2 F
5 C => 41.0 F
6 C => 42.8 F
7 C => 44.6 F
8 C => 46.4 F
9 C => 48.2 F
10 C => 50.0 F
11 C => 51.8 F
12 C => 53.6 F
13 C => 55.4 F
14 C => 57.2 F
15 C => 59.0 F
16 C => 60.8 F
17 C => 62.6 F
18 C => 64.4 F
19 C => 66.2 F
20 C => 68.0 F
21 C => 69.8 F
22 C => 71.6 F
23 C => 73.4 F
24 C => 75.2 F
25 C => 77.0 F
26 C => 78.8 F
27 C => 80.6 F
28 C => 82.4 F
29 C => 84.2 F
30 C => 86.0 F
31 C => 87.8 F
32 C => 89.6 F
33 C => 91.4 F
34 C => 93.2 F
35 C => 95.0 F
"""

task6 = "imperial_units.py"
input6 = "1.3\n"
expected6 = ("Enter a distance in meters: "
             "51.18 inch\n"
             "4.27 feet\n"
             "1.42 yards\n"
             "0.00 miles\n")

task7 = "trigonometry.py"
input7 = ""
expected7 = """radians |  sine | tangent
-------------------------
    0.0 |   0.0 |     0.0
    0.1 |   0.1 |     0.1
    0.2 |   0.2 |     0.2
    0.3 |   0.3 |    0.31
    0.4 |  0.39 |    0.42
    0.5 |  0.48 |    0.55
    0.6 |  0.56 |    0.68
    0.7 |  0.64 |    0.84
    0.8 |  0.72 |    1.03
    0.9 |  0.78 |    1.26
    1.0 |  0.84 |    1.56
    1.1 |  0.89 |    1.96
    1.2 |  0.93 |    2.57
    1.3 |  0.96 |     3.6
    1.4 |  0.99 |     5.8
    1.5 |   1.0 |    14.1
    1.6 |   1.0 |  -34.23
    1.7 |  0.99 |    -7.7
    1.8 |  0.97 |   -4.29
    1.9 |  0.95 |   -2.93
    2.0 |  0.91 |   -2.19
    2.1 |  0.86 |   -1.71
    2.2 |  0.81 |   -1.37
    2.3 |  0.75 |   -1.12
    2.4 |  0.68 |   -0.92
    2.5 |   0.6 |   -0.75
    2.6 |  0.52 |    -0.6
    2.7 |  0.43 |   -0.47
    2.8 |  0.33 |   -0.36
    2.9 |  0.24 |   -0.25
    3.0 |  0.14 |   -0.14
    3.1 |  0.04 |   -0.04
   3.14 |   0.0 |    -0.0
"""

task8 = "distance.py"
input8 = "3.0\n7.0\n-2.0\n3.0\n"
expected8 = ("First point's x-coordinate: "
             "First point's y-coordinate: "
             "Second point's x-coordinate: "
             "Second point's y-coordinate: "
             "The euclidean distance between the two points is 6.4031.\n")
input8_2 = "2.0\n0.0\n3.0\n3.0\n"
expected8_2 = ("First point's x-coordinate: "
               "First point's y-coordinate: "
               "Second point's x-coordinate: "
               "Second point's y-coordinate: "
               "The euclidean distance between the two points is 3.1623.\n")

task9 = "temperature_tables.py"
input9 = "C\n"
expected9 = ("For C => F enter C, for F => C enter F: "
"""-20 C => -4.0 F
-19 C => -2.2 F
-18 C => -0.4 F
-17 C => 1.4 F
-16 C => 3.2 F
-15 C => 5.0 F
-14 C => 6.8 F
-13 C => 8.6 F
-12 C => 10.4 F
-11 C => 12.2 F
-10 C => 14.0 F
-9 C => 15.8 F
-8 C => 17.6 F
-7 C => 19.4 F
-6 C => 21.2 F
-5 C => 23.0 F
-4 C => 24.8 F
-3 C => 26.6 F
-2 C => 28.4 F
-1 C => 30.2 F
0 C => 32.0 F
1 C => 33.8 F
2 C => 35.6 F
3 C => 37.4 F
4 C => 39.2 F
5 C => 41.0 F
6 C => 42.8 F
7 C => 44.6 F
8 C => 46.4 F
9 C => 48.2 F
10 C => 50.0 F
11 C => 51.8 F
12 C => 53.6 F
13 C => 55.4 F
14 C => 57.2 F
15 C => 59.0 F
16 C => 60.8 F
17 C => 62.6 F
18 C => 64.4 F
19 C => 66.2 F
20 C => 68.0 F
21 C => 69.8 F
22 C => 71.6 F
23 C => 73.4 F
24 C => 75.2 F
25 C => 77.0 F
26 C => 78.8 F
27 C => 80.6 F
28 C => 82.4 F
29 C => 84.2 F
30 C => 86.0 F
31 C => 87.8 F
32 C => 89.6 F
33 C => 91.4 F
34 C => 93.2 F
35 C => 95.0 F
36 C => 96.8 F
37 C => 98.6 F
38 C => 100.4 F
39 C => 102.2 F
40 C => 104.0 F
""")

total = 0
total += grade_by_io(task1, input1, expected1)
total += grade_by_io(task2, input2, expected2)
total += grade_by_io(task3, input3, expected3)
total += grade_by_io(task4, input4, expected4)
total += grade_by_io(task5, input5, expected5)
total += grade_by_io(task6, input6, expected6)
total += grade_by_io(task7, input7, expected7)
total += grade_by_io(task8, input8, expected8, 0.5)
total += grade_by_io(task8, input8_2, expected8_2, 0.5)
total += grade_by_io(task9, input9, expected9)

print()
print(total, "in total")
