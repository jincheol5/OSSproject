import pygame

from settings import *
from sprites import *

class Pause:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True #창 실행 Boolean 값
        self.return_playing = True # 리턴값
        self.returnNum = 3

        #마우스 포인터
        pygame.mouse.set_visible(False)
        self.mousePointer = MousePointer()
        self.pointer = pygame.sprite.Group()
        self.pointer.add(self.mousePointer)

        #텍스트
        self.text = Text(WIDTH/2,100, "PAUSED", 40, WHITE, MOVIE)
        self.startButtonText = Text(WIDTH/2, HEIGHT*4/5, "P L A Y", 40, BLACK, MOVIE)
        self.text_group = pygame.sprite.Group()
        self.text_group.add(self.text)
        self.text_group.add(self.startButtonText)

        #이미지
        self.image_group = pygame.sprite.Group()
        self.image_exit = Image(30, 30, WIDTH-50, 50, BUTTON_EXIT)
        self.image_group.add(self.image_exit)
        self.image_back = Image(30, 30, 50, 50, BUTTON_BACK)
        self.image_group.add(self.image_back)

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

        self.run()

        return self.return_playing, self.returnNum

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
                    self.return_playing = False
            #입력
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.return_playing = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if( self.startButton.button_clicked() ):
                    self.playing = False
                    self.return_playing = True
                elif( self.exitButton.button_clicked() ):
                    self.playing = False
                    self.return_playing = False
                    self.returnNum = 0
                elif( self.goBackButton.button_clicked() ):
                    self.playing = False
                    self.return_playing = False
                    self.returnNum = 3

    def update(self):
        #업데이트
        self.pointer.update()
        self.button_group.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.button_group.draw(self.screen)
        self.image_group.draw(self.screen)
        self.text_group.draw(self.screen)
        self.pointer.draw(self.screen)
        
        pygame.display.flip()


