#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict

def read_input(filename):
    return open(filename).readline().rstrip("\n")

def is_valid(new):
    for c in 'iol':
        if c in new:
            return False

    for i in range(2, len(new)):
        if ord(new[i - 2]) + 2 == ord(new[i - 1]) + 1 == ord(new[i]):
            break
    else:
        return False

    for i in range(1, len(new)):
        if new[i - 1] == new[i]:
            break
    else:
        return False

    for i in range(i + 2, len(new)):
        if new[i - 1] == new[i]:
            break
    else:
        return False

    return True

def next_pwd(password):
    codes = list(password[::-1])
    codes[0] = chr(ord(codes[0]) + 1)
    for i in range(len(codes)):
        if codes[i] > 'z':
            codes[i] = 'a'
            codes[i + 1] = chr(ord(codes[i + 1]) + 1)
    return ''.join(codes[::-1])
        

def part12(password):
    new = next_pwd(password)
    while not is_valid(new):
        new = next_pwd(new)
    return new

def main(filename):
    password = read_input(filename)
    new = part12(password)
    print(new)
    print(part12(new))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
