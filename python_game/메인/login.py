import os
import pygame

from settings import *
from sprites import *

class Login:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True #창 실행 Boolean 값
        self.returnNum = 2 # 리턴값
        self.ID = ''

        #마우스 포인터
        pygame.mouse.set_visible(False)
        self.mousePointer = MousePointer()
        self.pointer = pygame.sprite.Group()
        self.pointer.add(self.mousePointer)

        #텍스트
        self.text = Text(WIDTH/2,100, "로그인 화면", 40, BLACK, MOVIE)
        self.text2 = Text(WIDTH/2,250, "ENTER YOUR ID:", 30, BLACK, MOVIE)
        self.text_ID = Text(WIDTH/2,HEIGHT/2, self.ID , 40, RED, MOVIE)
        self.text_loginButton = Text(WIDTH/2, HEIGHT*4/5, "L O G I N", 40, BLACK, MOVIE)
        self.text_group = pygame.sprite.Group()
        self.text_group.add(self.text)
        self.text_group.add(self.text2)
        self.text_group.add(self.text_ID)
        self.text_group.add(self.text_loginButton)

        #이미지
        
        self.image_group = pygame.sprite.Group()

        #버튼
        self.startButton = Button(WIDTH/2, HEIGHT/8, WIDTH/2, HEIGHT*4/5, LIGHTGRAY)
        self.exitButton = Button(50, 50, WIDTH-50, 50, LIGHTGRAY)
        self.goBackButton = Button(50, 50, 50, 50, LIGHTGRAY)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.startButton)
        self.button_group.add(self.exitButton)
        self.button_group.add(self.goBackButton)

    def new(self):
        # start page
        self.ID = ''

        self.run()

        return (self.returnNum, self.ID)

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
                if event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    self.ID = self.ID[:-1]
                else :
                    pass
                    
            if event.type == pygame.TEXTINPUT:
                if len(self.ID) < ID_MAX:
                    self.ID += event.text

            if event.type == pygame.MOUSEBUTTONDOWN:
                if( self.startButton.button_clicked() ):
                    if(len(self.ID) > 0):
                        self.playing = False
                        self.returnNum = 3
                    else :
                        print("ENTER YOUR ID")
                elif( self.exitButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 0
                elif( self.goBackButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 1
          
                

    def update(self):
        # if 종료조건 달성 시
        #self.playing = False

        #업데이트
        self.pointer.update()
        self.button_group.update()
        self.text_ID.text_update(self.ID)
        pass

    def draw(self):
        self.screen.fill(WHITE)
        self.image_group.draw(self.screen)
        self.button_group.draw(self.screen)
        self.text_group.draw(self.screen)
        self.pointer.draw(self.screen)
        
        pygame.display.flip()


