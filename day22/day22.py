#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import heapq
import math
import sys
from collections import namedtuple

GameState = namedtuple('GameState', ['mana_spent', 'turn', 'boss_hp', 'player_hp', 'player_mana', 'timer_state'])

def read_input(filename):
    f = open(filename)
    hp = f.readline().split(" ")[-1]
    damage = f.readline().split(" ")[-1]
    return int(hp), int(damage)

def part12(boss_hp, boss_damage, extra_loss=0):
    player_hp = 50
    player_mana = 500
    start_state = [0, 0, 0]
    turn = 0
    mana_spent = 0

    queue = [GameState(mana_spent, turn, boss_hp, player_hp, player_mana, start_state)]
    while queue:
        mana_spent, turn, boss_hp, player_hp, player_mana, state = heapq.heappop(queue)
        state = state[:]
        if boss_hp <= 0:
            return mana_spent
        if turn % 2 == 0:
            player_hp -= extra_loss
        if player_hp == 0:
            continue
        armor_boost = 0
        if state[0] > 0:
            armor_boost += 7
            state[0] -= 1
        if state[1] > 0:
            boss_hp -= 3
            if boss_hp <= 0:
                return mana_spent
            state[1] -= 1
        if state[2] > 0:
            player_mana += 101
            state[2] -= 1
        if turn % 2 == 0:
            if player_mana >= 53:
                heapq.heappush(queue, GameState(mana_spent + 53, turn + 1, boss_hp - 4, player_hp, player_mana - 53, state[:]))
            if player_mana >= 73:
                heapq.heappush(queue, GameState(mana_spent + 73, turn + 1, boss_hp - 2, player_hp + 2, player_mana - 73, state[:]))
            if player_mana >= 113 and state[0] == 0:
                new_state = [6, state[1], state[2]]
                heapq.heappush(queue, GameState(mana_spent + 113, turn + 1, boss_hp, player_hp, player_mana - 113, new_state))
            if player_mana >= 173 and state[1] == 0:
                new_state = [state[0], 6, state[2]]
                heapq.heappush(queue, GameState(mana_spent + 173, turn + 1, boss_hp, player_hp, player_mana - 173, new_state))
            if player_mana >= 229 and state[2] == 0:
                new_state = [state[0], state[1], 5]
                heapq.heappush(queue, GameState(mana_spent + 229, turn + 1, boss_hp, player_hp, player_mana - 229, new_state))
        else:
            player_hp = max(player_hp - (boss_damage - armor_boost), 0)
            if player_hp > 0:
                heapq.heappush(queue, GameState(mana_spent, turn + 1, boss_hp, player_hp, player_mana, state[:]))
            else:
                pass
                #print("Losing after", turn, "spent", mana_spent)


def main(filename):
    hp, damage = read_input(filename)
    print(part12(hp, damage, 0))
    print(part12(hp, damage, 1))

if __name__ == '__main__':
    main('input' if len(sys.argv) == 1 else sys.argv[1])
