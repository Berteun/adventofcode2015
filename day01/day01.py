#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def read_input(filename):
    return open(filename).readline()

def part1(parens):
    return parens.count('(') - parens.count(')')

def part2(parens):
    floor = 0
    for i, c in enumerate(parens):
        if c == '(':
            floor += 1
        if c == ')':
            floor -= 1
        if floor < 0:
            return i + 1

def main(filename):
    parens = read_input(filename) 
    print(part1(parens))
    print(part2(parens))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
