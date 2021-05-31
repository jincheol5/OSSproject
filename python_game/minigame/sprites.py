import pygame
import os

from settings import *

image_dir = os.path.abspath('image')
font_dir = os.path.abspath('font')
sound_dir = os.path.abspath('sound')

class Text(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, text, size, color, font_name):
        super().__init__()
        self.font_dir = os.path.join(font_dir, font_name)
        self.font = pygame.font.Font(self.font_dir, size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.baseText = text
        self.text = text
        self.color = color
        self.baseColor = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def text_update(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def color_update(self, color):
        mouse = pygame.mouse.get_pos()
        if self.rect.left <= mouse[0] <=self.rect.right and self.rect.top <= mouse[1] <= self.rect.bottom :
            self.color = color
            self.image = self.font.render(self.text, True, self.color)
        else :
            self.color = self.baseColor
            self.image = self.font.render(self.text, True, self.color)

class Image(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, image_name):
        super().__init__()
        self.image_dir = os.path.join(image_dir, image_name)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(round(width), round(height))) #이미지 사이즈 변경
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y] 
       
class Sound:
    def __init__(self, sound_name):
        self.sound_dir = os.path.join(sound_dir, sound_name)
        self.sound = pygame.mixer.Sound(self.sound_dir)
        
class MousePointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_dir = os.path.join(image_dir, POINTER_1)
        self.image = pygame.image.load(self.image_dir)
        self.image = pygame.transform.scale(self.image,(POINTER_SIZE,POINTER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = pygame.mouse.get_pos()
    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()

class Button(pygame.sprite.Sprite):
    def __init__(self, width, height,pos_x,pos_y,color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y] 
        
        self.basecolor = color
        self.sound = Sound(BUTTON_1).sound

    def button_clicked(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.left <= mouse[0] <=self.rect.right and self.rect.top <= mouse[1] <= self.rect.bottom :
            self.sound.play()
            return 1
        else :
            return 0

    def update(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.left <= mouse[0] <=self.rect.right and self.rect.top <= mouse[1] <= self.rect.bottom :
            self.image.fill(GRAY)
          
        else:
            self.image.fill(self.basecolor)