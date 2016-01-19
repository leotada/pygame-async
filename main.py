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
from client import Client
import threading
import time


class Game():
    def __init__(self):
        pygame.init()
        # network
        self.client = Client()
        netThread = threading.Thread(target=self.update_network)
        netThread.start()
        
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
        
    def update_network(self):
        self.client.update("conectei")
        time.sleep(0.5)
        self.update_network()

Game()
