#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re

def read_input(filename):
    return [l.rstrip("\n") for l in open(filename)]

def part1(strings):
    return sum(len(s) - len(eval(s)) for s in strings)

def part2(strings):
    table = str.maketrans({ '"': '\\"', '\\': '\\\\' })
    return sum(len('"' + s.translate(table) + '"') - len(s) for s in strings)

def main(filename):
    strings = read_input(filename)
    print(part1(strings))
    print(part2(strings))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
