#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
import re
import json
from collections import defaultdict

number_re = re.compile('-?\d+')

def read_input(filename):
    return open(filename).read()

def part1(doc):
    return sum(int(m) for m in number_re.findall(doc))

def sum_numbers(js):
    tot = 0
    if isinstance(js, list):
        for elem in js:
            if isinstance(elem, (dict, list)):
                tot += sum_numbers(elem)
            elif isinstance(elem, int):
                tot += elem
            else:
                assert isinstance(elem, str)
    elif isinstance(js, dict):
        if "red" in js.values():
            return 0
        else:
            for k, v in js.items():
                if isinstance(k, int):
                    tot += elem
                if isinstance(v, (dict, list)):
                    tot += sum_numbers(v)
                elif isinstance(v, int):
                    tot += v
                else:
                    assert isinstance(v, str)

    return tot


def part2(doc):
    js = json.loads(doc)
    return sum_numbers(js)

def main(filename):
    doc = read_input(filename)
    print(part1(doc))
    print(part2(doc))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
