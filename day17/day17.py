#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict, namedtuple

def powerset(lst):
    return itertools.chain.from_iterable(itertools.combinations(lst, r) for r in range(len(lst)+1))

def read_input(filename):
    return [int(l.strip()) for l in open(filename)]

def part1(containers):
    return sum(1 for s in powerset(containers) if sum(s) == 150)

def part2(containers):
    min_cont = min(len(s) for s in powerset(containers) if sum(s) == 150)
    return sum(1 for s in powerset(containers) if sum(s) == 150 and len(s) == min_cont)

def main(filename):
    containers = read_input(filename)
    print(part1(containers))
    print(part2(containers))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
