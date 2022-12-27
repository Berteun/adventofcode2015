#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum
import hashlib
import sys

class Action(Enum):
    toggle = 0
    turn_on = 1
    turn_off = 2

@dataclass
class Instruction:
    action: Action 
    lower_x: int
    lower_y: int
    upper_x: int
    upper_y: int

def read_input(filename):
    instructions = []
    for l in open(filename):
        tokens = l.split(' ')
        lx, ly = (int(x) for x in tokens[-3].split(','))
        ux, uy = (int(x) for x in tokens[-1].split(','))
        if tokens[0] == "toggle":
            action = Action.toggle
        elif tokens[1] == "on":
            action = Action.turn_on
        elif tokens[1] == "off":
            action = Action.turn_off
        instructions.append(Instruction(action, min(lx, ux), min(ly, uy), max(lx, ux), max(ly, uy)))
    return instructions

def part1(instructions):
    grid = [[False] * 1000 for _ in range(1000)]
    for instr in instructions:
        for y in range(instr.lower_y, instr.upper_y + 1):
            for x in range(instr.lower_x, instr.upper_x + 1):
                if instr.action == Action.turn_on:
                    grid[y][x] = True
                if instr.action == Action.turn_off:
                    grid[y][x] = False
                if instr.action == Action.toggle:
                    grid[y][x] = not grid[y][x]
    return sum(sum(row) for row in grid)

def part2(instructions):
    grid = [[0] * 1000 for _ in range(1000)]
    for instr in instructions:
        for y in range(instr.lower_y, instr.upper_y + 1):
            for x in range(instr.lower_x, instr.upper_x + 1):
                if instr.action == Action.turn_on:
                    grid[y][x] += 1
                if instr.action == Action.turn_off:
                    grid[y][x] = max(grid[y][x] - 1, 0) 
                if instr.action == Action.toggle:
                    grid[y][x] += 2
    return sum(sum(row) for row in grid)

def main(filename):
    instructions = read_input(filename)
    print(part1(instructions))
    print(part2(instructions))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
