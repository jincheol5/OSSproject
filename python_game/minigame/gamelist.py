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
        self.textList = []
        self.textList.append(Text(WIDTH*1/4 + 32, HEIGHT*3/6-48, "SHOOTING", 30, WHITE, MOVIE))
        self.textList.append(Text(WIDTH*3/4 - 28, HEIGHT*3/6-48, "CANNON", 30, WHITE, MOVIE))
        self.textList.append(Text(WIDTH*1/4 + 32, HEIGHT*5/6-48, "TRASH", 30, WHITE, MOVIE))
        self.textList.append(Text(WIDTH*3/4 - 28, HEIGHT*5/6-48, "MONSTER", 30, WHITE, MOVIE))
        for self.i in range(0,4) :
            self.text_group.add(self.textList[self.i])
        self.textList.append(Text(WIDTH*1/4 + 30, HEIGHT*3/6-50, "SHOOTING", 30, RED, MOVIE))
        self.textList.append(Text(WIDTH*3/4 - 30, HEIGHT*3/6-50, "CANNON", 30, RED, MOVIE))
        self.textList.append(Text(WIDTH*1/4 + 30, HEIGHT*5/6-50, "TRASH", 30, RED, MOVIE))
        self.textList.append(Text(WIDTH*3/4 - 30, HEIGHT*5/6-50, "MONSTER", 30, RED, MOVIE))
        for self.i in range(4,8) :
            self.text_group.add(self.textList[self.i])
        
        #이미지
        self.image_group = pygame.sprite.Group()
        self.image_exit = Image(30, 30, WIDTH-50, 50, BUTTON_EXIT)
        self.image_group.add(self.image_exit)
        self.image_back = Image(30, 30, 50, 50, BUTTON_BACK)
        self.image_group.add(self.image_back)
        self.image = []
        self.image.append(Image(WIDTH/3, HEIGHT*3/10, WIDTH*1/4 + 30, HEIGHT*3/6-50, SHOOTING_GAME))
        self.image.append(Image(WIDTH/3, HEIGHT*3/10, WIDTH*3/4 - 30, HEIGHT*3/6-50, CANNON_GAME))
        self.image.append(Image(WIDTH/3, HEIGHT*3/10, WIDTH*1/4 + 30, HEIGHT*5/6-50, RHYTHM_GAME))
        self.image.append(Image(WIDTH/3, HEIGHT*3/10, WIDTH*3/4 - 30, HEIGHT*5/6-50, SNAKE_GAME))
        for self.i in range(0,4) :
            self.image_group.add(self.image[self.i])
        #버튼
        self.exitButton = Button(50, 50, WIDTH-50, 50, LIGHTGRAY)
        self.goBackButton = Button(50, 50, 50, 50, LIGHTGRAY)
        self.button_group = pygame.sprite.Group()

        self.button = []
        self.button.append(Button(WIDTH/3, HEIGHT*3/10, WIDTH*1/4 + 30, HEIGHT*3/6-50, LIGHTGRAY))
        self.button.append(Button(WIDTH/3, HEIGHT*3/10, WIDTH*3/4 - 30, HEIGHT*3/6-50, LIGHTGRAY))
        self.button.append(Button(WIDTH/3, HEIGHT*3/10, WIDTH*1/4 + 30, HEIGHT*5/6-50, LIGHTGRAY))
        self.button.append(Button(WIDTH/3, HEIGHT*3/10, WIDTH*3/4 - 30, HEIGHT*5/6-50, LIGHTGRAY))

        for self.i in range(0,4) :
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


