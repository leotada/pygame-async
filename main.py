#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2016 Leonardo <leonardo_tada@hotmail.com>
#  

background_image_filename = 'sushiplate.jpg' 
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from sprite import Sprite


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768), 0, 32)
        self.peixe = Sprite(self, sprite_image_filename)
        self.load()
        
    def load(self):
        self.background = pygame.image.load(background_image_filename).convert()
        self.peixe.load()
        self.update()
        
    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    
            self.draw()
                    
    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.peixe.draw()
        
        pygame.display.update()

Game()
