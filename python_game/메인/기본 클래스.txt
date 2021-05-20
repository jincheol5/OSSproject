import os
import pygame

from settings import *

class Login:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True #창 실행 Boolean 값

        self.returnNum = 2 # 리턴값

        #폰트
        self.dir = os.path.dirname(__file__)
        self.font_dir = os.path.join(self.dir, 'font')
        self.font = os.path.join(self.font_dir, MOVIE)

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
                if event.key == pygame.K_x:
                    self.playing = False
                    self.returnNum = 1

    def update(self):
        # if 종료조건 달성 시
        #self.playing = False
        pass

    def draw(self):
         self.screen.fill(WHITE)
         self.draw_text("로그인 화면", 40, BLACK, WIDTH/2, 10)
         pygame.display.flip()

        #화면에 텍스트 처리를 위한 메서드
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
        #render(text, antialias, color, background=None) -> Surface


