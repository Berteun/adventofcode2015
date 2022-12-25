#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import sys

def read_input(filename):
    return open(filename).readline().strip()

def part1(key):
    i = 0
    while True:
        if hashlib.md5(f"{key}{i}".encode('ascii')).hexdigest().startswith("00000"):
            return i
        i += 1

def part2(key):
    i = 0
    while True:
        if hashlib.md5(f"{key}{i}".encode('ascii')).hexdigest().startswith("000000"):
            return i
        i += 1

def main(filename):
    key = read_input(filename)
    print(part1(key))
    print(part2(key))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
