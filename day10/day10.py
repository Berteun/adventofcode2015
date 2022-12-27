#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict

def read_input(filename):
    return open(filename).readline().rstrip("\n")

def expand(seq):
    pos = 0
    new_seq = ''
    while pos < len(seq):
        end = pos
        while end < len(seq) and seq[pos] == seq[end]:
            end += 1
        new_seq += str((end - pos)) + seq[pos]
        pos = end
    return new_seq

def part1(seq):
    for _ in range(50):
        seq = expand(seq)
    return len(seq) 

def main(filename):
    seq = read_input(filename)
    print(part1(seq))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
