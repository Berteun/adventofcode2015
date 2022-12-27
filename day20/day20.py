#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
import sys
from collections import defaultdict

def read_input(filename):
    return int(open(filename).readline().strip())

def part1(presents):
    bound = presents // 10
    divisors = [1] * bound
    for n in range(2, bound):
        for x in range(n, bound, n):
            divisors[x] += n
    for i, d in enumerate(divisors):
        if d*10 >= presents:
            return i

def part2(presents):
    bound = presents // 10
    divisors = [1] * bound
    for n in range(2, bound):
        for x in list(range(n, bound, n))[:50]:
            divisors[x] += n
    for i, d in enumerate(divisors):
        if d*11 >= presents:
            return i
    
def main(filename):
    presents = read_input(filename)
    #print(part1(presents))
    print(part2(presents))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
