import pygame
import neat
import time
import os
import random

W_WIDTH = 600
W_HEIGHT = 800

BIRD_IMGS   = [1, 2, 3, 4]
PIPE_IMG    = 1
BASE_IMG    = 1
BKGR_IMG    = 1

class Bird:
    
    # GLOBAL CLASS VARIABLES
    IMGS            = BIRD_IMGS
    MAX_ROTATION    = 25
    ROT_VELOCITY    = 20
    ANIM_TIME       = 5
    
    def __init__(self, x, y):
        self.x          = x
        self.y          = y
        self.tilt       = 0
        self.tick_count = 0
        self.velocity   = 0
        self.height     = self.y
        self.img_count  = 0
        self.img        = self.IMGS[0]
        
    def jump(self):
        self.velocity   = -10.5
        self.tick_count = 0
        self.height     = self.y
        
    # def move(self):
    #     self.tick_count += 1
    #     self.x += 1
    #     self.y += 1
        
    