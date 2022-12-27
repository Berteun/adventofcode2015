#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import math
import sys
from collections import namedtuple

Tool = namedtuple('Tool', ['Cost', 'Damage', 'Armor'])

Weapons = {
    "Dagger": Tool(8, 4, 0),
    "Shortsword": Tool(10, 5, 0),
    "Warhammer": Tool(25, 6, 0),
    "Longsword": Tool(40, 7, 0),
    "Greataxe": Tool(74, 8, 0),
}

Armor = {
    "None": Tool(0, 0, 0),
    "Leather": Tool(13, 0, 1),
    "Chainmail": Tool(31, 0, 2),
    "Splintmail": Tool(53, 0, 3),
    "Bandedmail": Tool(75, 0, 4),
    "Platemail": Tool(102, 0, 5),
}

Rings = {
    "Damage +1": Tool(25, 1, 0),
    "Damage +2": Tool(50, 2, 0),
    "Damage +3": Tool(100, 3, 0),
    "Defense +1": Tool(20, 0, 1),
    "Defense +2": Tool(40, 0, 2),
    "Defense +3": Tool(80, 0, 3),
}

def read_input(filename):
    f = open(filename)
    hp = f.readline().split(" ")[-1]
    damage = f.readline().split(" ")[-1]
    armor = f.readline().split(" ")[-1]
    return int(hp), int(damage), int(armor)

def wins(hp, damage, armor, boss_hp, boss_damage, boss_armor):
    my_dam = max(1, damage - boss_armor)
    boss_dam = max(1, boss_damage - armor)
    my_rounds_needed = int(math.ceil(boss_hp / my_dam))
    boss_rounds_needed = int(math.ceil(hp/ boss_dam))
    return my_rounds_needed <= boss_rounds_needed

def part1(boss_hp, boss_damage, boss_armor):
    best_cost = 10_000
    for weapon in Weapons.values():
        for armor in Armor.values():
            for rings in itertools.chain.from_iterable(itertools.combinations(Rings.values(), r) for r in range(3)):
                cost = weapon.Cost + armor.Cost + sum(r.Cost for r in rings)
                damage = weapon.Damage + armor.Damage + sum(r.Damage for r in rings)
                my_armor = weapon.Armor + armor.Armor + sum(r.Armor for r in rings)
                if wins(100, damage, my_armor, boss_hp, boss_damage, boss_armor):
                    best_cost = min(best_cost, cost)
    return best_cost

def part2(boss_hp, boss_damage, boss_armor):
    worst_cost = 0
    for weapon in Weapons.values():
        for armor in Armor.values():
            for rings in itertools.chain.from_iterable(itertools.combinations(Rings.values(), r) for r in range(3)):
                cost = weapon.Cost + armor.Cost + sum(r.Cost for r in rings)
                damage = weapon.Damage + armor.Damage + sum(r.Damage for r in rings)
                my_armor = weapon.Armor + armor.Armor + sum(r.Armor for r in rings)
                if not wins(100, damage, my_armor, boss_hp, boss_damage, boss_armor):
                    worst_cost = max(worst_cost, cost)
    return worst_cost

def main(filename):
    hp, damage, armor = read_input(filename)
    print(part1(hp, damage, armor))
    print(part2(hp, damage, armor))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
