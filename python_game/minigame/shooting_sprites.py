import pygame
import os
import random

from settings import *
from sprites import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_name = JET_2
        self.width = 40
        self.height = 60
        self.speed_x = 0
        self.speed_y = 0
        # 이동 속도
        self.acc_x = 7
        self.acc_y = 7
        # 초기 위치
        self.pos_x = WIDTH / 2
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

        #객체가 이동 가능 구역을 넘어 갔을 시
        if self.rect.top < HEIGHT/2 :
            self.rect.top = HEIGHT/2
        if self.rect.bottom > HEIGHT :
            self.rect.bottom = HEIGHT
        if self.rect.left < self.width/2 :
            self.rect.left = self.width/2
        if self.rect.right > WIDTH - self.width/2:
            self.rect.right = WIDTH - self.width/2

        self.mask = pygame.mask.from_surface(self.image) #jet mask

class Meteor(pygame.sprite.Sprite):
    def __init__(self, meteorSpeed):
        super().__init__()
        self.image_name = METEOR
        self.width = 60
        self.height = 60
        self.speed_x = 0
        self.speed_y = meteorSpeed
        # 이동 속도
        self.acc_x = 0
        self.acc_y = 0
        # 초기 위치
        self.pos_x = random.randrange(self.width/2, WIDTH - self.width/2)
        self.pos_y = - self.height/2
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
        if self.rect.top > HEIGHT:
            self.kill()
        self.mask = pygame.mask.from_surface(self.image) #meteor mask

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_name = SPACESHIP
        self.width = 100
        self.height = 80
        self.speed_x = 3
        self.speed_y = 0
        # hit 
        self.explode_count = 20
        self.hit_count = 0
        # 이동 속도
        self.acc_x = 0
        self.acc_y = 0
        # 초기 위치
        self.pos_x = random.randrange(self.width/2, WIDTH - self.width/2)
        self.pos_y = self.height/2 + 30
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
        if self.rect.left <= 0 :
            self.speed_x = - self.speed_x
        if self.rect.right >= WIDTH:
            self.speed_x = - self.speed_x

        

        self.mask = pygame.mask.from_surface(self.image) #meteor mask

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image_name = BULLET
        self.width = 10
        self.height = 20
        self.speed_x = 0
        self.speed_y = -10
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