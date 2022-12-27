#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict

def read_input(filename):
    graph = defaultdict(dict)    
    for line in open(filename):
        tokens = line.strip().split(' ')
        graph[tokens[0]][tokens[2]] = int(tokens[4])
        graph[tokens[2]][tokens[0]] = int(tokens[4])
    return graph

def dist(graph, p):
    return sum(graph[p[i - 1]][p[i]] for i in range(1, len(p)))

def part1(graph):
    nodes = list(graph.keys())
    best = 1_000_000
    for p in itertools.permutations(nodes):
        best = min(best, dist(graph, p))
    return best

def dist(graph, p):
    return sum(graph[p[i - 1]][p[i]] for i in range(1, len(p)))

def part2(graph):
    nodes = list(graph.keys())
    best = 0
    for p in itertools.permutations(nodes):
        best = max(best, dist(graph, p))
    return best

def main(filename):
    graph = read_input(filename)
    print(part1(graph))
    print(part2(graph))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
