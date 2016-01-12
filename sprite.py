#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sprite.py
#  
#  Copyright 2016 Leonardo <leonardo_tada@hotmail.com>
#  

import pygame
from gameobjects.vector2 import Vector2


class Sprite():
    def __init__(self, game, image_name):
        self.game = game
        self.image = None
        self.image_name = image_name
        self.position = Vector2()
        
    def load(self):
        self.image = pygame.image.load(self.image_name).convert_alpha()
        
    def update(self):
        pass

    def draw(self):
        self.game.screen.blit(self.image, self.position.value)
