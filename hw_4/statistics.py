#!/usr/bin/env python3

"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

"""
This module contains functions to compute the statistical values
of a given column in a given csv file.
"""

import argparse
import math
import sys


def items(filename):
    """Return one line at a time as dictionary.

    The first line has to be a header that can be used as dictionary keys. All
    numeric values in the input file are automatically converted to float.
    Calling this generator function again after the last line restarts at the
    top.
    """
    with open(filename, encoding='utf-8-sig') as f:
        header = [e.strip() for e in f.readline().split(',')]
        for line in f:
            if not line.strip():
                continue
            columns = line.split(',')
            item = dict(zip(header, columns))
            for key in item:
                try:
                    item[key] = float(item[key])
                except:
                    pass
            yield item


def count(filename):
    """Return the number of items in the given file."""
    num_items = 0
    for item in items(filename):
        num_items += 1
    return num_items


def find_min(filename,key):
    """Return the min value for given filename and key (column in csv file)"""
    num_list = []
    for item in items(filename):
        num_list.append(item[key])
    num_list.sort()
    return num_list[0]


def find_max(filename,key):
    """Return the max value for given filename and key (column in csv file)"""
    num_list = []
    for item in items(filename):
        num_list.append(item[key])
    num_list.sort()
    return num_list[len(num_list) - 1]

def calc_mean(filename, key):
    """Return the average value for given filename and key (column in csv file)"""
    mean = 0
    for item in items(filename):
        mean +=float((item[key]))
    mean = mean / count(filename)
    return mean


def calc_stddev(filename, key):
    """Return the standard deviation value for given filename and key (column in csv file)

    Standard deviation is the measure of dispersion of a set of data from its mean. ... Standard Deviation is also known as volatility. It gives a sense of how dispersed the data in a sample is from the mean.
    """
    stddev = 0
    mean = calc_mean(filename, key)
    for item in items(filename):
        stddev = stddev + (item[key] - mean)**2
    stddev = math.sqrt(stddev / count(filename))
    return stddev

def calc_sum(filename, key):
    """
    Return the sum for given filename and key (column in csv file)
    """
    sum = 0
    for item in items(filename):
        sum +=float(item[key])
    return sum


def calc_variance(filename, key):
    """Return the variance for given filename and key (column in csv file)

    Variance measures how far each number in the set is from the mean and thus from every other number in the set.
    """
    variance = 0
    mean = calc_mean(filename, key)
    for item in items(filename):
        variance = variance + (item[key] - mean)**2
    variance = variance / count(filename)
    return variance

def calc_median(filename, key):
    """
    Return the middle number in a sorted list of number for given filename and key (column in csv file)
    """
    median_list = []
    median_formula = 0
    for item in items(filename):
        median_list.append(item[key])
    median_list.sort()
    median_formula = count(filename) // 2;
    return(median_list[median_formula])


'''
[4.63, 4.83, 4.9, 5.05, 5.07, 5.1, 5.1, 5.15, 5.35, 5.4, 5.55, 5.58, 5.6, 5.85, 5.99, 6.08, 6.15, 6.25, 6.29, 6.3, 6.4, 6.5, 6.6, 6.6, 6.67, 6.7, 6.7, 6.7, 6.7, 6.7, 6.75, 6.75, 6.8, 6.85, 6.85, 6.87, 6.88, 6.9, 6.96, 6.97, 7.1, 7.12, 7.15, 7.4, 7.5, 7.51, 7.6]
'''



def main():
    """
    Entry point if the module is started as designated program.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Text file to be analyzed.")
    parser.add_argument("key",
                        help="Name of the column that should be analyzed.")
    args = parser.parse_args()

    print("count:\n", count(args.filename))
    print("sum:", calc_sum(args.filename, args.key))
    print("mean:", calc_mean(args.filename, args.key))
    print("variance:", calc_variance(args.filename, args.key))
    print("standard deviation:", calc_stddev(args.filename, args.key))
    print("median:", calc_median(args.filename, args.key))

if __name__ == "__main__":
    sys.exit(main())
