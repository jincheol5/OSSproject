import pygame
import time

from settings import *
from sprites import *
from monster_sprites import *
from pause import *
from startpage import *
from board import *

class Monster:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True #창 실행 Boolean 값
        self.returnNum = 3 # 리턴값
        #마우스 포인터
        pygame.mouse.set_visible(False)
        #텍스트
        self.text_score = Text(WIDTH/2, 50, "SCORE : ", 30, WHITE, MOVIE)
        self.text_eat = Text(WIDTH/2, 100, "EAT : ", 20, BLUE, MOVIE)
        self.text_group = pygame.sprite.Group()
        self.text_group.add(self.text_score)
        self.text_group.add(self.text_eat)
        #시작화면 텍스트
        self.text_name = "MONSTER"
        self.text_explain = "먹이를 먹고 몬스터를 키워주세요"
        self.text_score_explain = "먹이를 먹으면 점수 + 100"
        self.text_key = "상하좌우 방향키로 움직이세요"
        self.text_exit = "UFO나 장애물에 부딛히면 GAME OVER"
        #이미지
        self.backGround = Image(WIDTH, HEIGHT, WIDTH/2, HEIGHT/2, SPACE)
        self.image_group = pygame.sprite.Group()
        self.image_group.add(self.backGround)

    def new(self,ID):
        # start page
        self.ID = ID
        self.playTime = 0
        self.score = 0
        self.enemySpeed = 3
        self.count_eat = 1
        self.count = 0
        self.enemy_appear = False
        self.enemy_time = 0

        self.player_group = pygame.sprite.Group() # 플레이어
        self.food_group = pygame.sprite.Group() # 먹이 그룹
        self.enemy_group = pygame.sprite.Group() # 적 그룹
        self.obstacle_group = pygame.sprite.Group() # 장애물 그룹

        self.player = Player() # Player 선언
        self.food = Food() # food 선언
        self.obstacle_1 = Obstacle()
        self.obstacle_2 = Obstacle()
        self.obstacle_3 = Obstacle()
        self.food_group.add(self.food)
        self.player_group.add(self.player)
        self.obstacle_group.add(self.obstacle_1)
        self.obstacle_group.add(self.obstacle_2)
        self.obstacle_group.add(self.obstacle_3)
        #sound
        self.sound_eat = Sound(EAT).sound
        self.BGM = Sound(SNAKE_BGM).sound
        self.BGM.set_volume(0.5)
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

    def update(self):
        # 플레이 시간 증가
        self.playTime += 1
        if (self.enemy_appear):
            self.enemy_time += 1
        # enemy 등장 (10 개 먹을 때 마다)
        if(self.count_eat %11 == 0 and self.count_eat!=0) :
            self.enemy = Enemy() # Enemy 선언
            self.enemy_group.add(self.enemy)
            self.enemy_appear = True
            self.count_eat += 1
        # 사이즈 업 (player와 food 충돌)
        self.eat = pygame.sprite.spritecollide(self.player, self.food_group, True, pygame.sprite.collide_mask)
        if self.eat:
            self.player.size_up()
            self.score += 100
            self.count_eat += 1
            self.count += 1
            self.food = Food()
            self.food_group.add(self.food)
            self.sound_eat.play()

        # 게임 오버
        self.gameOver = pygame.sprite.spritecollide(self.player, self.enemy_group, False, pygame.sprite.collide_mask)
        self.gameOver_2 = pygame.sprite.spritecollide(self.player, self.obstacle_group, False, pygame.sprite.collide_mask)
        if self.gameOver or self.gameOver_2:
            self.playing = False
            time.sleep(1.0)
            self.board = Board(4, self.ID, self.score)
            self.returnNum = self.board.new()
            del(self.board)
        # 스프라이트 업데이트
        self.player_group.update() 
        self.food_group.update()
        self.enemy_group.update()

        #업데이트
        self.text_score.text_update(self.text_score.baseText + str(self.score))
        self.text_eat.text_update(self.text_eat.baseText + str(self.count))

    def draw(self):
        self.screen.fill(BLACK)
        # 오브젝트
        self.food_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.player_group.draw(self.screen)
        self.obstacle_group.draw(self.screen)
        self.text_group.draw(self.screen)
        
        pygame.display.flip()
