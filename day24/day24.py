#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import math
import sys

def read_input(filename):
    return [int(line.strip()) for line in open(filename)]

def generate_groups(packages, target_weight):
    packages = sorted(packages)
    packages_needed = 1 + target_weight // packages[-1]
    solutions = []
    while not solutions:
        for comb in itertools.combinations(packages, packages_needed):
            if sum(comb) == target_weight:
                solutions.append((math.prod(comb), set(comb)))
        packages_needed += 1
    solutions.sort()
    return solutions

def part1(packages):
    group_weight = sum(packages) // 3
    s = set(packages)
    for (qe, used) in generate_groups(packages, group_weight):
        unused = s - used
        for _ in generate_groups(unused, sum(unused) // 2):
            return qe

def part2(packages):
    group_weight = sum(packages) // 4
    s = set(packages)
    for (qe, used) in generate_groups(packages, group_weight):
        unused = s - used
        for (_, used_2) in generate_groups(unused, sum(unused) // 3):
            unused_2 = unused - used_2
            for _ in generate_groups(unused, sum(unused_2) // 2):
                return qe

def main(filename):
    packages = read_input(filename)
    print(part1(packages))
    print(part2(packages))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
