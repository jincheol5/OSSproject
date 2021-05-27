import pygame
import os
import random

from settings import *
from sprites import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_name = MONSTER
        self.width = 30
        self.height = 30
        self.speed_x = 0
        self.speed_y = 0
        # 이동 속도
        self.acc_x = 4
        self.acc_y = 4
        # 초기 위치
        self.pos_x = WIDTH / 2
        self.pos_y = HEIGHT - self.height
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.baseImage = pygame.image.load(self.image_dir)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #객체가 이동 가능 구역을 넘어 갔을 시
        if self.rect.top < 0 :
            self.rect.top = 0
        if self.rect.bottom > HEIGHT :
            self.rect.bottom = HEIGHT
        if self.rect.left < 0 :
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        self.mask = pygame.mask.from_surface(self.image) #jet mask

    def size_up(self): 
        self.width += 2
        self.height += 2
        self.pos_x = self.rect.center[0]
        self.pos_y = self.rect.center[1]
        self.image = pygame.transform.scale(self.baseImage,(round(self.width), round(self.height))) #이미지 사이즈 변경
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_name = FOOD
        self.width = 30
        self.height = 30
        # 초기 위치
        self.pos_x = random.randrange(self.width/2 + 10 , WIDTH - self.width/2 - 10)
        self.pos_y = random.randrange(self.height/2 + 50, HEIGHT - self.height/2 - 50)
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def update(self):
        self.mask = pygame.mask.from_surface(self.image) #meteor mask

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_name = UFO
        self.width = 50
        self.height = 50
        self.speed_x = 3
        self.speed_y = 3
        # hit 
        self.explode_count = 20
        self.hit_count = 0
        # 이동 속도
        self.acc_x = 3
        self.acc_y = 3
        # 초기 위치
        self.pos_x = WIDTH - self.width/2 - 10
        self.pos_y = self.height/2 + 10
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
        elif self.rect.right >= WIDTH:
            self.speed_x = - self.speed_x
        if self.rect.top <= 0 :
            self.speed_y = - self.speed_y
        elif self.rect.bottom >= HEIGHT :
            self.speed_y = - self.speed_y

        self.mask = pygame.mask.from_surface(self.image) #meteor mask

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_name = METEOR
        self.width = 20
        self.height = 20
        # 초기 위치
        self.pos_x = random.randrange(self.width/2 + 10 , WIDTH - self.width/2 - 10)
        self.pos_y = random.randrange(self.height/2 + 50, HEIGHT - self.height/2 - 50)
        # 이미지 초기화
        self.image_dir = os.path.join(image_dir, self.image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(self.width), round(self.height))) #이미지 사이즈 변경
        # 위치 초기화
        self.rect = self.image.get_rect()
        self.rect.center = [self.pos_x, self.pos_y] 

    def update(self):
        self.mask = pygame.mask.from_surface(self.image) #meteor mask
