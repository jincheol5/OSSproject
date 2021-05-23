import pygame
import random
import time
from datetime import datetime

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400,600]
screen = pygame.display.set_mode(size)

title = "My Game"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정

clock = pygame.time.Clock()
color = (170,210,230)

#게임시간 playTime
playTime=0

#총알 쿨타임
bulletTime=0

#운석 속도
meteorSpeed = 3
#초당 운석 나오는 빈도수
meteorFreq = 3

#킬스코어
killScore = 0

#obj 객체 (클래스)
class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0

    #이미지 불러오기
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else :
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
    #사이즈 변경
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img,(sx,sy))
        self.sx, self.sy = self.img.get_size()
    #그리기
    def show(self):
        screen.blit(self.img, (self.x,self.y))

#충돌 함수
def crash(a,b):
    if (a.x - b.sx <= b.x) and (b.x <= a.x + a.sx):
        if (a.y - b.sy <= b.y) and (b.y <= a.y + a.sy):
            return True
        else:
            return False
    else :
        return False

#제트기 선언
jet = obj()
jet.put_img(r"C:\Users\82106\OneDrive\사진\image\jet.png")
jet.change_size(30,50)
jet.x = round(size[0]/2)-round(jet.sx/2)
jet.y = round(size[1]-jet.sy-30)
jet.move = 4

#총알 리스트 
bullet_list = []
#운석 리스트
meteor_list = []

#키 on off
up_go = False
down_go = False
left_go = False
right_go = False
space_go = False

# 4-0. 게임 시작 대기
startSB = 0
while startSB == 0:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
            startSB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
               SB = 0
               startSB = 1
    
    screen.fill(color)
    font = pygame.font.SysFont(None,40)
    text_start = font.render("Press Z to Start",True,(0,0,0))
    screen.blit(text_start,(round(size[0]/2)-100, round(size[1]/2)))
    
    pygame.display.flip()


# 4. 메인 이벤트

startTime = datetime.now().replace(microsecond = 0)

while SB == 0:


    # 4-1. FPS 설정
    clock.tick(60)

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_go = True
            if event.key == pygame.K_DOWN:
                down_go = True
            if event.key == pygame.K_LEFT:
                left_go = True
            if event.key == pygame.K_RIGHT:
                right_go = True
            if event.key == pygame.K_z:
                space_go = True
                #총알 쿨타임 초기화
                bulletTime = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_go = False
            if event.key == pygame.K_DOWN:
                down_go = False
            if event.key == pygame.K_LEFT:
                left_go = False
            if event.key == pygame.K_RIGHT:
                right_go = False
            if event.key == pygame.K_z:
                space_go = False


    # 4-3. 입력, 시간에 따른 변화
    playTime+=1
    
    nowTime = datetime.now().replace(microsecond = 0)
    deltaTime = (nowTime - startTime)

    # 방향키 상하좌우 (제트기 상하좌우로 움직임)
    if up_go == True:
        jet.y -= jet.move
        
    if down_go == True:
        jet.y += jet.move
    
    if left_go == True:
        jet.x -= jet.move
        
    if right_go == True:
        jet.x += jet.move
    
    #스페이스바 (총알 발사)
    if space_go == True and bulletTime%8 == 0:
        bullet = obj()
        bullet.put_img(r"C:\Users\82106\OneDrive\사진\image\bullet.png")
        bullet.change_size(10,20)
        bullet.x = round(jet.x + jet.sx/2 - bullet.sx/2)
        bullet.y = jet.y - bullet.sy + 5
        bullet.move = 10
        bullet_list.append(bullet)
    
    bulletTime += 1

    
    #삭제 리스트
    d_list = []

    # 1초마다 랜덤 운석 생성
    if playTime%round(60/meteorFreq) == 0:
        meteor = obj()
        meteor.put_img(r"C:\Users\82106\OneDrive\사진\image\meteor.png")
        meteor.change_size(40,40)
        meteor.x = random.randrange(round(jet.sx/2),size[0]-round(meteor.sx/2)-round(jet.sx/2))
        meteor.y = -meteor.sy
        meteor.move = meteorSpeed
        meteor_list.append(meteor)
    #운석 움직임
    for i in range(len(meteor_list)):
        meteor = meteor_list[i]
        meteor.y += meteor.move

        #운석이 화면을 넘어가면 삭제
        if meteor.y >= size[1]:
            d_list.append(i)

    d_list.reverse()
    for d in d_list:
        del meteor_list[d]

    #삭제 리스트
    d_list = []

    #총알 움직임
    for i in range(len(bullet_list)):
        bullet = bullet_list[i]
        bullet.y -= bullet.move

        #총알이 화면을 넘어가면 삭제
        if bullet.y <= -bullet.sy:
            d_list.append(i)

    d_list.reverse()
    for d in d_list:
        del bullet_list[d]

    #제트기 행동반경 제한
    #위
    if jet.y <= round(size[1]*3/5):
        jet.y = round(size[1]*3/5)
    #아래
    if jet.y >= size[1] - jet.sy:
        jet.y = size[1] - jet.sy
    #왼쪽
    if jet.x <= 0:
        jet.x = 0
    #오른쪽
    if jet.x >= size[0] - jet.sx:
        jet.x = size[0] - jet.sx

    #총알-운석 충돌판정
    db_list=[]
    dm_list=[]
    for i in range(len(bullet_list)):
        for j in range(len(meteor_list)):
            bullet = bullet_list[i]
            meteor = meteor_list[j]
            if crash(bullet,meteor) == True:
                db_list.append(i)
                dm_list.append(j)
    db_list = list(set(db_list))
    dm_list = list(set(dm_list))

    db_list.reverse()
    for db in db_list:
        del bullet_list[db]
    dm_list.reverse()
    for dm in dm_list:
        del meteor_list[dm]
        killScore += 1

    #운석-제트기 충돌판정
    for i in range(len(meteor_list)):
        meteor = meteor_list[i]
        if crash(jet,meteor) == True :
            SB = 1
            time.sleep(1)
            

    # 4-4. 그리기
    screen.fill(color)
    jet.show()
    for bullet in bullet_list:
        bullet.show()
    for meteor in meteor_list:
        meteor.show()
    
    #텍스트
    font = pygame.font.SysFont(None,20)
    text_kill = font.render("KILL SCORE : {}".format(killScore),True,(0,0,0))
    screen.blit(text_kill,(10,5))

    text_time = font.render("PLAY TIME : {}".format(deltaTime),True,(0,0,0))
    screen.blit(text_time,(size[0]-150,5))

    # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임 종료
pygame.quit()

