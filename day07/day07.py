#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum
import hashlib
import sys


class LitNode:
    def __init__(self, n):
        self.n = n 

    def eval(self, _d):
        return self.n

class ExtNode:
    def __init__(self, n):
        self.n = n 
        self.cache = None

    def eval(self, d):
        if self.cache is None:
            self.cache = d[self.n].eval(d)
        return self.cache

class AndNode:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.cache = None

    def eval(self, d):
        if self.cache is None:
            self.cache = self.lhs.eval(d) & d[self.rhs].eval(d)
        return self.cache


class OrNode:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.cache = None

    def eval(self, d):
        if self.cache is None:
            self.cache = self.lhs.eval(d) | d[self.rhs].eval(d)
        return self.cache

class NotNode:
    def __init__(self, node):
        self.node = node
        self.cache = None


    def eval(self, d):
        if self.cache is None:
            self.cache = ~d[self.node].eval(d) & 65535
        return self.cache
    
class LshiftNode:
    def __init__(self, lhs, amount):
        self.lhs = lhs
        self.amount = amount
        self.cache = None

    def eval(self, d):
        if self.cache is None:
            self.cache = (d[self.lhs].eval(d) << self.amount) & 65535
        return self.cache

class RshiftNode:
    def __init__(self, lhs, amount):
        self.lhs = lhs
        self.amount = amount
        self.cache = None

    def eval(self, d):
        if self.cache is None:
            self.cache = d[self.lhs].eval(d) >> self.amount
        return self.cache

def read_input(filename):
    d = {}
    for line in open(filename):
        tokens = line.strip().split(" ")
        dest = tokens[-1]
        instr = tokens[:-2]
        if len(instr) == 3:
            if instr[1] == "AND":
                if instr[0].isdigit():
                    lhs = LitNode(int(instr[0]))
                else:
                    lhs = ExtNode(instr[0])
                d[dest] = AndNode(lhs, instr[2])
            elif instr[1] == "OR":
                if instr[0].isdigit():
                    lhs = LitNode(int(instr[0]))
                else:
                    lhs = ExtNode(instr[0])
                d[dest] = OrNode(lhs, instr[2])
            elif instr[1] == "LSHIFT":
                d[dest] = LshiftNode(instr[0], int(instr[2]))
            elif instr[1] == "RSHIFT":
                d[dest] = RshiftNode(instr[0], int(instr[2]))
            else:
                assert False
        if len(instr) == 2:
            if instr[0] == "NOT":
                d[dest] = NotNode(instr[1])
            else:
                assert False
        if len(instr) == 1:
            if instr[0].isdigit():
                d[dest] = LitNode(int(instr[0]))
            else:
                d[dest] = ExtNode(instr[0])
    return d

def part1(d):
    return d["a"].eval(d)    

def part2(d, ans):
    d["b"] = LitNode(ans)
    return d["a"].eval(d)

def main(filename):
    d = read_input(filename)
    ans = part1(d)
    print(ans)
    d = read_input(filename)
    print(part2(d, ans))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
