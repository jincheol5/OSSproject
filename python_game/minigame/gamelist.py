import os
import pygame

from settings import *
from sprites import *

class GameList:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True #창 실행 Boolean 값
        self.returnNum = 1 # 리턴값

        #마우스 포인터
        pygame.mouse.set_visible(False)
        self.mousePointer = MousePointer()
        self.pointer = pygame.sprite.Group()
        self.pointer.add(self.mousePointer)

        #텍스트
        self.text = Text(WIDTH/2,100, "게임 리스트", 40, BLACK, MOVIE)
        self.text_group = pygame.sprite.Group()
        self.text_group.add(self.text)
        #이미지
        self.image_group = pygame.sprite.Group()

        #버튼
        self.exitButton = Button(50, 50, WIDTH-50, 50, LIGHTGRAY)
        self.goBackButton = Button(50, 50, 50, 50, LIGHTGRAY)
        self.button_group = pygame.sprite.Group()

        self.button = []
        self.i = 0
        for self.i in range(0,4) :
            self.button.append(Button(WIDTH/2, HEIGHT/8, WIDTH/2, HEIGHT*(2+self.i)/6, LIGHTGRAY))
            self.button_group.add(self.button[self.i])
        
        self.button_group.add(self.exitButton)
        self.button_group.add(self.goBackButton)

    def new(self):
        # start page

        self.run()

        return self.returnNum

    def run(self):
        # page loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # page loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                    self.returnNum = 0
            #입력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                if( self.button[0].button_clicked() ):
                    self.playing = False
                    self.returnNum = 4
                elif( self.button[1].button_clicked() ):
                    self.playing = False
                    self.returnNum = 5
                elif( self.button[2].button_clicked() ):
                    self.playing = False
                    self.returnNum = 6
                elif( self.button[3].button_clicked() ):
                    self.playing = False
                    self.returnNum = 7
                
                elif( self.exitButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 0
                elif( self.goBackButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 2
                #mouse = pygame.mouse.get_pos()
                #if self.button.pressed(mouse):   #Button's pressed method is called
                #   print ('button hit')

    def update(self):
        # if 종료조건 달성 시
        #self.playing = False

        #업데이트
        self.pointer.update()
        self.button_group.update()

        pass

    def draw(self):
        self.screen.fill(WHITE)
        self.image_group.draw(self.screen)
        self.button_group.draw(self.screen)
        self.text_group.draw(self.screen)
        self.pointer.draw(self.screen)
        
        pygame.display.flip()


