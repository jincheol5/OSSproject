import pygame
import os
import random

from settings import *
from sprites import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_name = CANNON
        self.width = 60
        self.height = 60
        self.speed_x = 0
        self.speed_y = 0
        # 이동 속도
        self.acc_x = 3
        self.acc_y = 3
        # 초기 위치
        self.pos_x = self.width
        self.pos_y = HEIGHT - self.height
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_dir = os.path.join(image_dir, CROSSHAIR)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(POINTER_SIZE,POINTER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class LeftWall(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image_name = METEOR
        self.width = 2
        self.height = HEIGHT
        # 초기 위치
        self.pos_x = -10
        self.pos_y = HEIGHT/2
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y]

class Meteor(pygame.sprite.Sprite):
    def __init__(self,meteorSpeed):
        super().__init__()
        self.image_name = PLANE
        self.width = 80
        self.height = 60
        self.speed_x = meteorSpeed
        self.speed_y = 0
        # 이동 속도
        self.acc_x = -1
        self.acc_y = 0
        # 초기 위치
        self.pos_x = WIDTH + self.width/2
        self.pos_y = random.randrange(self.height, round(HEIGHT * 2/3))
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #객체가 이동 가능 구역을 넘어 갔을 시
        if self.rect.right < 0:
            self.kill()

        self.mask = pygame.mask.from_surface(self.image) #meteor mask

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, aim_x, aim_y):
        super().__init__()
        self.image_name = BULLET
        self.width = 20
        self.height = 20
        self.speed_x = ( (aim_x - pos_x)/ 30 )
        self.speed_y = ( (aim_y - pos_y)/ 30 )
        # 이동 속도
        self.acc_x = 0
        self.acc_y = 0
        # 초기 위치
        self.pos_x = pos_x
        self.pos_y = pos_y - self.height/2
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #객체가 이동 가능 구역을 넘어 갔을 시
        if self.rect.bottom < 0:
            self.kill()
        self.mask = pygame.mask.from_surface(self.image) #bullet mask