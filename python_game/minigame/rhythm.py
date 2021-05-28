import pygame
import time

from settings import *
from sprites import *
from rhythm_sprites import *
from pause import *
from startpage import *
from board import *

class Rhythm:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True #창 실행 Boolean 값
        self.returnNum = 3 # 리턴값

        #마우스 포인터
        pygame.mouse.set_visible(False)

        #텍스트
        self.text_score = Text(WIDTH/2, 50, "SCORE : ", 30, WHITE, MOVIE)
        self.text_life = Text(WIDTH/2, 100, "LIFE : ", 25, RED, MOVIE)
        self.text_group = pygame.sprite.Group()
        self.text_group.add(self.text_score)
        self.text_group.add(self.text_life)

        #시작화면 텍스트
        self.text_name = "RHYTHM"
        self.text_explain = "타이밍에 맞춰 쓰레기를 치워주세요"
        self.text_score_explain = "쓰레기를 처리하면 점수 + 10"
        self.text_key = " A S D  J K L 를 타이밍에 맞춰 입력하세요"
        self.text_exit = "LIFE가 0이 되면 GAME OVER"

        #이미지
        self.backGround = Image(WIDTH, HEIGHT, WIDTH/2, HEIGHT/2, SPACE)
        self.image_group = pygame.sprite.Group()
        self.image_group.add(self.backGround)

    def new(self,ID):
        # start page
        self.ID = ID
        self.playTime = 0
        self.score = 0
        self.life = 10
        # object
        self.bottom = Bottom() # 바닥
        self.meteor_group = pygame.sprite.Group() # 운석 그룹
        self.player_button_group = pygame.sprite.Group() # 운석 그룹
        self.player_button = []
        for self.i  in range(0,6):
            self.player_button.append( Player_Button(self.i,GRAY) )
            self.player_button_group.add(self.player_button[self.i])

        #sound
        self.BGM = Sound(CANNON_BGM_2).sound
        self.BGM.set_volume(0.5)
        self.BGM_BPM = 180 / 60
        # BGM 시작
        self.BGM.play(-1)
        # run
        self.run()
        # BGM 종료
        self.BGM.stop()
        return self.returnNum

    def run(self):
        self.playing = True
        startpage = Startpage(self.text_name, self.text_explain, self.text_score_explain, self.text_key, self.text_exit)
        self.playing, self.returnNum = startpage.new()
        del(startpage)
        # page loop
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
                if event.key == pygame.K_a:
                    self.player_button[0].button_down()
                    self.hit(0)
                if event.key == pygame.K_s:
                    self.player_button[1].button_down()
                    self.hit(1)
                if event.key == pygame.K_d:
                    self.player_button[2].button_down()
                    self.hit(2)
                if event.key == pygame.K_j:
                    self.player_button[3].button_down()
                    self.hit(3)
                if event.key == pygame.K_k:
                    self.player_button[4].button_down()
                    self.hit(4)
                if event.key == pygame.K_l:
                    self.player_button[5].button_down()
                    self.hit(5)

                if event.key == pygame.K_ESCAPE:
                    self.p = Pause()
                    self.playing, self.returnNum = self.p.new()
                    del(self.p)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player_button[0].button_up()
                if event.key == pygame.K_s:
                    self.player_button[1].button_up()
                if event.key == pygame.K_d:
                    self.player_button[2].button_up()
                if event.key == pygame.K_j:
                    self.player_button[3].button_up()
                if event.key == pygame.K_k:
                    self.player_button[4].button_up()
                if event.key == pygame.K_l:
                    self.player_button[5].button_up()

    def update(self):
        # 플레이 시간 증가
        self.playTime += 1
        # 메테오 추가
        if(self.playTime <300):
            pass
        elif( self.playTime % 20  == 0):
            self.meteor = Meteor()
            self.meteor_group.add(self.meteor)

        # life 감소 (meteor 가 바닥에 닿음)
        self.miss = pygame.sprite.spritecollide(self.bottom, self.meteor_group, True, pygame.sprite.collide_mask)
        if self.miss:
            self.life -= 1

        # 게임 오버 (life == 0)
        if self.life == 0:
            self.playing = False
            time.sleep(1.0)
            self.board = Board(3, self.ID, self.score)
            self.returnNum = self.board.new()
            del(self.board)

        # 스프라이트 업데이트
        self.meteor_group.update()

        #업데이트
        self.text_score.text_update(self.text_score.baseText + str(self.score))
        self.text_life.text_update(self.text_life.baseText + str(self.life))

    def draw(self):
        self.screen.fill(BLACK)
        # 오브젝트
        self.player_button_group.draw(self.screen)
        self.meteor_group.draw(self.screen)
        self.text_group.draw(self.screen)
        
        pygame.display.flip()

    def hit(self, index):
        self.player_button[index].button_down()
        self.hitted = pygame.sprite.spritecollide(self.player_button[index], self.meteor_group, True, pygame.sprite.collide_mask)
        if (self.hitted):
            self.score += 10