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

print(bg)

ind_e = []

ind_y = 0
for y in bg:
    ind_x = 0
    for x in y:
        if x == 'e':
            ind_e.append((ind_y, ind_x))
        ind_x += 1
    ind_y += 1
        
# r = random.choice(ind_e)
# print(r)

class Objs:
    def __init__(self, name):
        self.name = name
        self.position = ()

l2 = list(ind_e)

O1 = Objs("O1")
O2 = Objs("O2")
O3 = Objs("O3")
G = Objs("G")

OO = [O1, O2, O3, G]

for O in OO:
    r = random.choice(l2)
    O.position = r
    l2.remove(r)

print(O1.position)
print(O2.position)
print(O3.position)
print(G.position)

l2 == ind_e
print(l2)
print(ind_e)

import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(0,3)
	
	#Re-collage
	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, position_perso)
	#Rafraichissement
	pygame.display.flip()
