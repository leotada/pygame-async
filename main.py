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
from network import Network
import threading
import time
import json
from gameobjects.vector2 import Vector2


pos = [0,0]
username = input("Nome de usuario: ")
network_received = None



class Game():
    def __init__(self):
        pygame.init()
        # network
        self.network = Network()
        self.network.connect()
        self.network.login(username)
        netThread = threading.Thread(target=self.update_network)
        netThread.start()
        
        self.screen = pygame.display.set_mode((1024, 768), 0, 32)
        #self.peixe = Sprite(self, sprite_image_filename)
        self.load()
        
    def load(self):
        self.background = pygame.image.load(background_image_filename).convert()
        #self.peixe.load()
        self.update()
        
    def update(self):
        global pos
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    pos[0] += 5
            self.draw()
                    
    def draw(self):
        self.screen.blit(self.background, (0,0))
        #self.peixe.draw()
        
        # network data draw
        if network_received is not None:
            received = json.loads(network_received)
            for player in received:
                xe = Sprite(self, sprite_image_filename)
                xe.load()
                xe.position = Vector2(player['pos'][0], player['pos'][1])
                xe.draw()
        
        pygame.display.update()
        
    def update_network(self):
        global network_received
        data = {'action': 'update', 'id': username, 'pos': pos}
        network_received = self.network.update(json.dumps(data))
        time.sleep(0.5)
        return self.update_network()

Game()
