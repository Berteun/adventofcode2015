#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

m = {'^': -1j, 'v': 1j, '<': -1, '>': 1}

def read_input(filename):
    return [m[c] for c in open(filename).readline()]

def part1(directions):
    visited = set()
    location = 0
    for d in directions:
        visited.add(location)
        location += d
    visited.add(location)
    return len(visited)

def part2(directions):
    visited = set()
    santa_location = 0
    robo_location = 0
    for i, d in enumerate(directions):
        if i % 2:
            santa_location += d
        else:
            robo_location += d
        visited.add(santa_location)
        visited.add(robo_location)
    visited.add(santa_location)
    visited.add(robo_location)
    return len(visited)

def main(filename):
    directions = read_input(filename)
    print(part1(directions))
    print(part2(directions))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
