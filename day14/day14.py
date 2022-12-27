#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict, namedtuple

Reindeer = namedtuple('Reindeer', ['speed', 'active', 'rest'])

def read_input(filename):
    deer = {}
    for line in open(filename):
        tokens = line.strip().split(' ')
        deer[tokens[0]] = Reindeer(int(tokens[3]), int(tokens[6]), int(tokens[-2]))
    return deer

def part1(table, n=2503):
    dist = {}
    for name, deer in table.items():
        period = deer.active + deer.rest
        np, rem = divmod(n, period)
        dist[name] = (np * deer.active + min(deer.active, rem)) * deer.speed
    max_dist = max(dist.values())
    return max_dist, [deer for deer in dist if dist[deer] == max_dist]

def part2(table):
    points = defaultdict(int)
    for n in range(1, 2504):
        _, all_deer = part1(table, n)
        for deer in all_deer:
            points[deer] += 1
    return max(points.values())

def main(filename):
    table = read_input(filename)
    print(part1(table)[0])
    print(part2(table))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
