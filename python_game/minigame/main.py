import pygame
import sys

from settings import *
from start import *
from login import *
from gamelist import *

from shooting import *
from cannon import *
from rhythm import *
from snake import *


def main():
    # initialize game window, etc
    pygame.init()
    pygame.display.set_caption(TITLE)   

    ID = ''
    running = 1
    BGM = Sound(HAPPY).sound
    BGM.set_volume(0.3)
    BGM.play()

    while running:
        #시작화면
        if running == 1:
            start = Start()
            running = start.new()
            del(start)
        #로그인
        elif running == 2:
            login = Login()
            (running,ID) = login.new()
            print(ID)
            del(login)
        #게임 리스트
        elif running == 3:
            gamelist = GameList()
            running = gamelist.new()
            del(gamelist)
        #게임1
        elif running == 4:
            BGM.stop()
            game = Shooting()
            running = game.new(ID)
            del(game)
            BGM.play()
        #게임2
        elif running == 5: 
            BGM.stop()
            game = Cannon()
            running = game.new(ID)
            del(game)
            BGM.play()
        #게임3
        elif running == 6:  
            BGM.stop()
            game = Rhythm()
            running = game.new(ID)
            del(game)
            BGM.play()
        #게임4
        elif running == 7:  
            BGM.stop()
            game = Snake()
            running = game.new(ID)
            del(game)
            BGM.play()

    pygame.quit()
    sys.exit()

if __name__ == '__main__': main()