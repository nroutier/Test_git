#! /usr/bin/env python3
# coding: utf-8

import random

bg = []

with open("level.txt", "r") as level:
    for row in level:
        line = []
        for char in row:
            if char != '\n':
                line.append(char)
        bg.append(line)

# print(bg)

ind_e = []

for y in bg:
    for x in y:
        if x == 'e':
            ind_e.append((bg.index(y), y.index(x)))

# r = random.choice(ind_e)
# print(r)

class Objs:
    def __init__(self, name):
        self.name = name
        self.position = ()

O1 = Objs("O1")
O2 = Objs("O2")
O3 = Objs("O3")
G = Objs("G")

OO = [O1, O2, O3, G]

for O in OO:
    r = random.choice(ind_e)
    O.position = r
    ind_e.remove(r)

print(O1.position)
print(O2.position)
print(O3.position)
print(G.position)