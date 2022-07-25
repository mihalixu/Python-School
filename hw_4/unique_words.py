#!/usr/bin/env python3

"""
.. moduleauthor:: Mihael Subasic <mihael.subasic@bulme.at>
"""

import argparse
import sys
from collections import namedtuple

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Text file to be analyzed.")
    args = parser.parse_args()
    with open(args.infile, encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    count_unique(words)
    count_unique_sorted()

def count_unique(words):
    """
    Takes list of words as input and outputs sorted dict. with their ocurences
    """
    words_dict = {}
    wordsArray = []
    textArray = []
    ocurences = 0

    for text_element in words:
        text_element = text_element.strip(",").strip(".").lower()
        textArray.append(text_element)
        if text_element not in wordsArray and text_element != "":
            wordsArray.append(text_element)

    wordsArray.sort()
    for word in wordsArray:
        ocurences = 0
        for textword in textArray:
            if textword == word:
                ocurences +=1
        words_dict[word] = ocurences
    return words_dict


def count_unique_sorted(words):
    """
    Takes list of words as input and outputs list of named tupels
    """

    tupleArray = []
    wordsArray = []
    textArray = []
    ocurences = 0

    for text_element in words:
        text_element = text_element.strip(",").strip(".").lower()
        textArray.append(text_element)
        if text_element not in wordsArray and text_element != "":
            wordsArray.append(text_element)

    for tupel_word in wordsArray:
        ocurences = 0
        for textword in textArray:
            if textword == tupel_word:
                ocurences +=1
        Tupel = namedtuple('Tupel', ['word','count'])
        t = Tupel(tupel_word, ocurences)
        tupleArray.append((t[0],t[1]))
    return tupleArray


if __name__ == "__main__":
    sys.exit(main())
