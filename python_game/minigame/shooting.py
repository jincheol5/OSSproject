import pygame
import time

from settings import *
from sprites import *
from shooting_sprites import *
from pause import *
from startpage import *
from board import *

class Shooting:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True #창 실행 Boolean 값
        self.returnNum = 3 # 리턴값

        #마우스 포인터
        pygame.mouse.set_visible(False)

        #텍스트
        self.text_score = Text(WIDTH/2, 50, "SCORE : ", 30, WHITE, MOVIE)
        self.text_group = pygame.sprite.Group()
        self.text_group.add(self.text_score)

        #시작화면 텍스트
        self.text_name = "SHOOTING"
        self.text_explain = "운석을 피해 적 군함을 터트리세요"
        self.text_score_explain = "적 군함을 터트리면 점수 + 1000"
        self.text_key = "상하좌우 방향키로 움직이세요!"
        self.text_exit = "운석과 충돌하면 GAME OVER"

        #이미지
        self.backGround = Image(WIDTH, HEIGHT, WIDTH/2, HEIGHT/2, SPACE)
        self.image_group = pygame.sprite.Group()
        self.image_group.add(self.backGround)

    def new(self,ID):
        # start page
        self.ID = ID
        self.playTime = 0
        self.score = 0
        self.meteorSpeed = 3

        self.player_group = pygame.sprite.Group() # 플레이어
        self.meteor_group = pygame.sprite.Group() # 운석 그룹
        self.bullet_group = pygame.sprite.Group() # 총알 그룹
        self.enemy_group = pygame.sprite.Group() # 적 그룹

        self.player = Player() # Player 선언
        self.enemy = Enemy() # Enemy 선언

        self.player_group.add(self.player)
        self.enemy_group.add(self.enemy)

        #sound
        self.sound_explode = Sound(EXPLODE).sound
        self.sound_fire = Sound(FIRE_SOUND).sound
        self.BGM = Sound(CANNON_BGM_2).sound
        self.BGM.set_volume(0.3)
        self.sound_fire.set_volume(0.1)
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
                if event.key == pygame.K_LEFT:
                    self.player.speed_x -= self.player.acc_x
                if event.key == pygame.K_RIGHT:
                    self.player.speed_x += self.player.acc_x
                if event.key == pygame.K_UP:
                    self.player.speed_y -= self.player.acc_y
                if event.key == pygame.K_DOWN:
                    self.player.speed_y += self.player.acc_y
                
                if event.key == pygame.K_ESCAPE:
                    self.player.speed_x = 0
                    self.player.speed_y = 0
                    self.p = Pause()
                    self.playing, self.returnNum = self.p.new()
                    del(self.p)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.speed_x += self.player.acc_x
                if event.key == pygame.K_RIGHT:
                    self.player.speed_x -= self.player.acc_x
                if event.key == pygame.K_UP:
                    self.player.speed_y += self.player.acc_y
                if event.key == pygame.K_DOWN:
                    self.player.speed_y -= self.player.acc_y
                
                #mouse = pygame.mouse.get_pos()
                #if self.button.pressed(mouse):   #Button's pressed method is called
                #   print ('button hit')

    def update(self):
        # 플레이 시간 증가
        self.playTime += 1
        if self.playTime%10 == 0 :
            self.score += 1

        #30초마다 메테오 속도 증가
        if(self.playTime%1800 == 0):
            self.meteorSpeed += 3
        # 메테오 추가
        if(self.playTime % 60 == 0):
            self.meteor = Meteor(self.meteorSpeed)
            self.meteor_group.add(self.meteor)
        # 총알 추가
        if(self.playTime % 15 == 0):
            self.bullet = Bullet(self.player.rect.center[0], self.player.rect.top)
            self.bullet_group.add(self.bullet)

        # enemy 파괴 (n번 이상 hit 시)
        if self.enemy.hit_count >= self.enemy.explode_count:
            self.enemy.kill()
            self. score += 1000

            self.sound_explode.play()

            self.enemy = Enemy() 
            self.enemy_group.add(self.enemy)

        # enemy와 bullet 충돌
        self.collide_eb = pygame.sprite.spritecollide(self.enemy, self.bullet_group, True, pygame.sprite.collide_mask)
        if self.collide_eb:
            self.enemy.hit_count += 1
            self.sound_fire.play()

        # 게임 오버 (player와 meteor 충돌)
        self.gameover = pygame.sprite.spritecollide(self.player, self.meteor_group, False, pygame.sprite.collide_mask)
        if self.gameover:
            self.playing = False
            time.sleep(1.0)
            self.board = Board(1, self.ID, self.score)
            self.returnNum = self.board.new()
            del(self.board)

        # 스프라이트 업데이트
        self.player_group.update() 
        self.meteor_group.update()
        self.bullet_group.update()
        self.enemy_group.update()

        #업데이트
        self.text_score.text_update(self.text_score.baseText + str(self.score))

    def draw(self):
        self.screen.fill(BLACK)

        # 오브젝트
        self.meteor_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.player_group.draw(self.screen)

        self.text_group.draw(self.screen)
        
        pygame.display.flip()


