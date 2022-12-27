#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from collections import defaultdict, namedtuple

Ingredient = namedtuple('Ingredient', ['capa', 'dura', 'flav', 'text', 'calo'])

def read_input(filename):
    ingredients = {}
    for line in open(filename):
        tokens = line.strip().replace(', ', ' ').replace(': ', ' ').split(' ')
        ingredients[tokens[0]] = Ingredient(int(tokens[2]), int(tokens[4]), int(tokens[6]), int(tokens[8]), int(tokens[10]))
    return ingredients

def part12(table, calo_goal=None):
    ingredients = list(table.values())
    max_score = 0
    for combination in itertools.combinations_with_replacement(ingredients, 100):
        capa = sum(ing.capa for ing in combination)
        dura = sum(ing.dura for ing in combination)
        flav = sum(ing.flav for ing in combination)
        text = sum(ing.text for ing in combination)
        calo = sum(ing.calo for ing in combination)
        score = max(0, capa) * max(0, dura) * max(0, flav) * max(0, text)
        if score > max_score:
            if calo_goal is None or calo == calo_goal:
                max_score = score
    return max_score

def main(filename):
    table = read_input(filename)
    print(part12(table))
    print(part12(table, 500))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
