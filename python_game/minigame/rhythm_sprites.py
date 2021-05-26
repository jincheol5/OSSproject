import pygame
import os
import random

from settings import *
from sprites import *


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = WIDTH/6
        self.height = HEIGHT/6
        self.speed_x = 0
        self.speed_y = 12
        # 이동 속도
        self.acc_x = 0
        self.acc_y = 0
        # 초기 위치
        self.pos_x = random.randrange(1,7) * WIDTH/6 - self.width/2
        self.pos_y = - self.height/2
        # 이미지 초기화
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #객체가 이동 가능 구역을 넘어 갔을 시
        if self.rect.top > HEIGHT + 300:
            self.kill()
        self.mask = pygame.mask.from_surface(self.image) #meteor mask

class Player_Button(pygame.sprite.Sprite):
    def __init__(self, num, color):
        super().__init__()
        self.width = WIDTH/6 - 2
        self.height = HEIGHT/20
        # 초기 위치
        self.pos_x = num * WIDTH/6 + WIDTH/12
        self.pos_y = HEIGHT * 7/8 - self.height/2
        # 이미지 초기화
        self.baseColor = color
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def button_down(self):
        self.image.fill(RED)

    def button_up(self):
        self.image.fill(self.baseColor)

    def update(self):
        pass

class Bottom(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image_name = METEOR
        self.width = WIDTH
        self.height = 2
        # 초기 위치
        self.pos_x = WIDTH/2
        self.pos_y = HEIGHT + 100
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y]