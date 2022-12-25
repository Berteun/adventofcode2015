#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def read_input(filename):
    return [tuple((int(n) for n in l.strip().split('x'))) for l in open(filename)]

def part1(dimensions):
    return sum(2*(l*w + w*h + h*l) + min(l*w, w*h, h*l) for (l,w,h) in dimensions)

def part2(dimensions):
    return sum(l*w*h + min(2*l + 2*h, 2*l + 2*w, 2* h + 2*w) for (l,w,h) in dimensions)

def main(filename):
    dimensions = read_input(filename)
    print(part1(dimensions))
    print(part2(dimensions))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
