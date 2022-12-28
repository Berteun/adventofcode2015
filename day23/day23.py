#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def read_input(filename):
    return [line.replace(", ", " ").strip().split(" ") for line in open(filename)]

def part12(instructions, r_a):
    r = { 
        "a": r_a,
        "b": 0,
    }
    ip = 0
    while True:
        instr = instructions[ip]
        if instr[0] == "hlf":
            r[instr[1]] //= 2
            ip += 1
        elif instr[0] == "tpl":
            r[instr[1]] *= 3
            ip += 1
        elif instr[0] == "inc":
            r[instr[1]] += 1
            ip += 1
        elif instr[0] == "jmp":
            ip += int(instr[1])
        elif instr[0] == "jie":
            if r[instr[1]] % 2 == 0:
                ip += int(instr[2])
            else:
                ip += 1
        elif instr[0] == "jio":
            if r[instr[1]] == 1:
                ip += int(instr[2])
            else:
                ip += 1
        if ip < 0 or ip >= len(instructions):
            break
    return r["b"]

def main(filename):
    instructions = read_input(filename)
    print(part12(instructions, 0))
    print(part12(instructions, 1))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
