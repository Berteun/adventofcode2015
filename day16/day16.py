#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict, namedtuple

Ingredient = namedtuple('Ingredient', ['capa', 'dura', 'flav', 'text', 'calo'])

analysis = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
def read_input(filename):
    sues = []
    for line in open(filename):
        tokens = line.strip().replace(', ', ' ').replace(': ', ' ').split(' ')
        sues.append({tokens[i] : int(tokens[i + 1]) for i in range(2, len(tokens), 2)})
    return sues

def part1(sues):
    real_sues = [i + 1 for i,sue in enumerate(sues) if all(analysis[k] == v for k, v in sue.items())]
    assert len(real_sues) == 1, "too many aunts found"
    return real_sues[0]

def part2(sues):
    real_sues = []
    for i, sue in enumerate(sues):
        for k, v in sue.items():
            if k in ("cats", "trees"):
                if analysis[k] >= v:
                    break
            elif k in ("pomeranians", "goldfish"):
                if analysis[k] <= v:
                    break
            else:
                if analysis[k] != v:
                    break
        else:
            real_sues.append(i + 1)
    assert len(real_sues) == 1, "too many aunts found"
    return real_sues[0]

def main(filename):
    sues = read_input(filename)
    print(part1(sues))
    print(part2(sues))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
