#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from enum import Enum
import hashlib
import sys

def read_input(filename):
    return [[c for c in l.strip()] for l in open(filename)]

def print_grid(grid):
    print('\n'.join(''.join(row) for row in grid))
    print()

def nb_on(grid, x, y):
    cnt = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            cx = x + dx
            cy = y + dy
            if cx < 0 or cx >= len(grid[0]) or cy < 0 or cy >= len(grid):
                continue
            cnt += (grid[cy][cx] == '#')
    return cnt

def evolve(grid):
    new_grid = [row[:] for row in grid]
    for y in range(len(grid)): 
        for x in range(len(grid[y])):
            n = nb_on(grid, x, y)
            if grid[y][x] == '#':
                if n != 2 and n != 3:
                    new_grid[y][x] = '.'
            else:
                if n == 3:
                    new_grid[y][x] = '#'
    return new_grid

def part1(grid):
    for n in range(100):    
        grid = evolve(grid)
    return sum(c == '#' for row in grid for c in row)

def part2(grid):
    grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1] = '#', '#', '#', '#'
    for n in range(100):    
        grid = evolve(grid)
        grid[0][0], grid[0][-1], grid[-1][0], grid[-1][-1] = '#', '#', '#', '#'
    return sum(c == '#' for row in grid for c in row)

def main(filename):
    grid = read_input(filename)
    print(part1(grid))

    grid = read_input(filename)
    print(part2(grid))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
