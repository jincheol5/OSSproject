import pygame

from settings import *
from sprites import *

class Start:
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
        self.text = Text(WIDTH/2,100, "미니게임 오락실", 40, BLUE, MOVIE)
        self.startButtonText = Text(WIDTH/2, HEIGHT*4/5, "S T A R T", 40, WHITE, MOVIE)
        self.text_group = pygame.sprite.Group()
        self.text_group.add(self.text)
        self.text_group.add(self.startButtonText)
        #이미지
        self.image = Image(WIDTH/2, HEIGHT/2-50, WIDTH/2, HEIGHT/2-30, BACKGROUND)
        self.image_group = pygame.sprite.Group()
        self.image_group.add(self.image)
        self.image_exit = Image(30, 30, WIDTH-50, 50, BUTTON_EXIT)
        self.image_group.add(self.image_exit)
        #버튼
        self.startButton = Button(WIDTH/2, HEIGHT/8, WIDTH/2, HEIGHT*4/5, BLACK)
        self.exitButton = Button(50, 50, WIDTH-50, 50, LIGHTGRAY)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.startButton)
        self.button_group.add(self.exitButton)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if( self.startButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 2
                elif( self.exitButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 0

    def update(self):
        #업데이트
        self.pointer.update()
        self.button_group.update()

    def draw(self):
        self.screen.fill(WHITE)
        self.button_group.draw(self.screen)
        self.image_group.draw(self.screen)
        self.text_group.draw(self.screen)
        self.pointer.draw(self.screen)
        
        pygame.display.flip()


