#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import math
import sys

def read_input(filename):
    tokens = open(filename).readline().replace(", ", " ").rstrip(".\n").split(" ")
    return int(tokens[-3]), int(tokens[-1])

def part1(row, column):
    code_no = (row + column - 2) * (row + column - 1) // 2 + column
    #for row in range(1, 10):
    #    for column in range(1, 10):
    #        p, q = row, column
    #        code_no = (p + q - 2) * (p + q - 1) //2 + q
    #        print("%4d" % code_no, "%10d" % ((20151125 * pow(252533, code_no - 1, 33554393)) % 33554393), sep=" ", end="")
    #    print()
    return ((20151125 * pow(252533, code_no - 1, 33554393)) % 33554393)

def main(filename):
    (row, column) = read_input(filename)
    print(part1(row, column))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
