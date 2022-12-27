#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict

def read_input(filename):
    table = defaultdict(dict)    
    for line in open(filename):
        tokens = line.strip().rstrip('.').split(' ')
        table[tokens[0]][tokens[-1]] = int(tokens[3]) * (-1 if tokens[2] == "lose" else 1)
    return table

def score(table, p):
    s = 0
    for i in range(len(p)):
        pers  = p[i]
        left  = p[(i - 1) % len(p)]
        right = p[(i + 1) % len(p)]
        s += table[pers][left] + table[pers][right]
    return s

def part1(table):
    nodes = list(table.keys())
    best = 0
    for p in itertools.permutations(nodes):
        best = max(best, score(table, p))
    return best

def part2(table):
    for k in list(table.keys()):
        table[k]["me"] = 0
        table["me"][k] = 0
    return part1(table)

def main(filename):
    table = read_input(filename)
    print(part1(table))
    print(part2(table))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
