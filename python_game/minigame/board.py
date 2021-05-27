import os
from config import url

import pygame
import requests
import json

from settings import *
from sprites import *

class Board:

    

    
    
    
    def __init__(self, NUMBER, ID, SCORE):
        #######################################
        #서버 db 불러오는 부분 

        # NUMBER (슈팅 1, 캐논 2, 리듬 3, 뱀 4)
        # ID
        # SCORE

        def makeboard(r):
          #문자열에서 불필요한 요소들 제거
          r=r.replace(" ",'')
          r=r.replace(",",'')
          r=r.replace("(",'')
          r=r.replace(")",'')
          r=r.lstrip("'")
          #'로 문자열 분리 
          board=r.split("'")
          return board


        #입력할 값 
        datas={
          
          'name':'jjm',
          'score':1234560
          
        }


        response=requests.post(url,data=datas)
        r=response.json()




        board=makeboard(r)
        name=[]
        score=[]


        for i in range(len(board)):
            if i%2==0: name.append(board[i])
            else: score.append(int(board[i]))

        #######################################












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
        self.text = Text(WIDTH/2+1,51, "RANKING", 40, WHITE, MOVIE)
        self.text2 = Text(WIDTH/2,50, "RANKING", 40, RED, MOVIE)
        
        #순위 아이디 점수 
        self.q1 = Text(WIDTH/10*2,150, "순위", 30, RED, MOVIE)
        self.q2 = Text(WIDTH/2,150, "id", 30, RED, MOVIE)
        self.q3 = Text(WIDTH/10*8,150, "점수", 30, RED, MOVIE)

        self.textlist_rank=[]
        self.textlist_name=[]
        self.textlist_score=[]
        h=200
        for i in range(len(name)):
          if i==0:
            self.textlist_rank.append(Text(WIDTH/10*2,h, "%2dst"%(i+1), 25, YELLOW, MOVIE))
            self.textlist_name.append(Text(WIDTH/2,h, "%s"%(name[i]), 25, YELLOW, MOVIE))
            self.textlist_score.append(Text(WIDTH/10*8,h, "%d"%(score[i]), 25, YELLOW, MOVIE))
          elif i==1:
            self.textlist_rank.append(Text(WIDTH/10*2,h, "%2dnd"%(i+1), 25, GRAY, MOVIE))
            self.textlist_name.append(Text(WIDTH/2,h, "%s"%(name[i]), 25, GRAY, MOVIE))
            self.textlist_score.append(Text(WIDTH/10*8,h, "%d"%(score[i]), 25, GRAY, MOVIE))
          elif i==2:
            self.textlist_rank.append(Text(WIDTH/10*2,h, "%2drd"%(i+1), 25, BROWN, MOVIE))
            self.textlist_name.append(Text(WIDTH/2,h, "%s"%(name[i]), 25, BROWN, MOVIE))
            self.textlist_score.append(Text(WIDTH/10*8,h, "%d"%(score[i]), 25, BROWN, MOVIE))
          else:
            self.textlist_rank.append(Text(WIDTH/10*2,h, "%2dth"%(i+1), 20, WHITE, MOVIE))
            self.textlist_name.append(Text(WIDTH/2,h, "%s"%(name[i]), 20, WHITE, MOVIE))
            self.textlist_score.append(Text(WIDTH/10*8,h, "%d"%(score[i]), 20, WHITE, MOVIE))
          h+=40 

        #내 점수
        self.myscore1=Text(WIDTH/10*2,600, "myscore", 25, BLUE, MOVIE)
        self.myscore2=Text(WIDTH/2,600, "%s"%(datas['name']), 25, BLUE, MOVIE)
        self.myscore3=Text(WIDTH/10*8,600, "%d"%(datas['score']), 25, BLUE, MOVIE)

        self.text_group = pygame.sprite.Group()


        self.text_group.add(self.text)
        self.text_group.add(self.text2)
        self.text_group.add(self.q1)
        self.text_group.add(self.q2)
        self.text_group.add(self.q3)
        for i in range(len(name)):
          self.text_group.add(self.textlist_rank[i])
          self.text_group.add(self.textlist_name[i])
          self.text_group.add(self.textlist_score[i])
        self.text_group.add(self.myscore1)
        self.text_group.add(self.myscore2)
        self.text_group.add(self.myscore3)
        

        #버튼
        
        self.exitButton = Button(50, 50, WIDTH-50, 50, LIGHTGRAY)
        self.goBackButton = Button(50, 50, 50, 50, LIGHTGRAY)

        self.button_group = pygame.sprite.Group()
        
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if( self.exitButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 0
                elif( self.goBackButton.button_clicked() ):
                    self.playing = False
                    self.returnNum = 3
                

    def update(self):
        # if 종료조건 달성 시
        #self.playing = False

        #업데이트
        self.pointer.update()
        
        self.button_group.update()

        

    def draw(self):
        self.screen.fill(BLACK)
        
        self.button_group.draw(self.screen)
        self.text_group.draw(self.screen)
        self.pointer.draw(self.screen)
        
        pygame.display.flip()


