#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import sys

def read_input(filename):
    return [l.strip() for l in open(filename)]

def part1(lines):
    tot = 0
    for l in lines:
        nice = True
        if len([c for c in l if c in ('a','e','i','o','u')]) < 3:
            nice = False
        for n in range(len(l) - 1):
            if l[n] == l[n + 1]:
                break
        else:
            nice = False
        for s in ('ab', 'cd', 'pq', 'xy'):
            if s in l:
                nice = False
        tot += nice
    return tot

def part2(lines):
    tot = 0
    for l in lines:
        nice = True
        for n in range(len(l) - 2):
            if l.find(l[n:n+2], n + 2) > -1:
                break
        else:
            nice = False
        for n in range(len(l) - 2):
            if l[n] == l[n + 2]:
                break
        else:
            nice = False
        tot += nice
    return tot

def main(filename):
    lines = read_input(filename)
    print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
