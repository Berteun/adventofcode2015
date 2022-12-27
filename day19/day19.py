#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
import sys
from collections import defaultdict

def read_input(filename):
    replacements, molecule = open(filename).read().split("\n\n")
    d = defaultdict(list)
    for rep in replacements.strip().split("\n"): 
        source, target = rep.strip().split(' => ')
        d[source].append(target)
    return d, molecule.strip()

def part1(reps, molecule):
    possible = set()
    for k in reps:
        for v in reps[k]:
            last_index = 0
            while True:
                last_index = molecule.find(k, last_index)
                if last_index == -1:
                    break
                possible.add(molecule[:last_index] + v + molecule[last_index + len(k):])
                last_index += 1
    return len(possible)

def part2(reps, start):
    rev_reps = { r : k for k, v in reps.items() for r in v }
    by_length = sorted(list(rev_reps.keys()), reverse=True, key=lambda x: len(x))

    def replace_longest(cur):
        for k in by_length:
            if (cnt := cur.count(k)) > 0:
                return cnt, cur.replace(k, rev_reps[k])

    steps = 0
    while start != "e":
        cnt, start = replace_longest(start)
        steps += cnt

    return steps


def main(filename):
    reps, molecule = read_input(filename)
    print(part1(reps, molecule))
    print(part2(reps, molecule))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
