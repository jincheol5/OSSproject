import pygame
import sys

from settings import *
from start import *
from login import *
from gamelist import *

from shooting import *
from cannon import *
from rhythm import *


def main():
    # initialize game window, etc
    pygame.init()
    pygame.display.set_caption(TITLE)   

    ID = ''
    SCORE = {1:0, 2:0, 3:0, 4:0}
    running = 1
    BGM = Sound(HAPPY).sound
    BGM.play()

    while running:
        #시작화면
        if running == 1:
            s = Start()
            running = s.new()
            del(s)
        #로그인
        elif running == 2:
            l = Login()
            (running,ID) = l.new()
            print(ID)
            del(l)
        #게임 리스트
        elif running == 3:
            gl = GameList()
            running = gl.new()
            del(gl)
        #게임1
        elif running == 4:
            BGM.stop()
            game = Shooting()
            running = game.new()
            del(game)
            BGM.play()
        #게임2
        elif running == 5: 
            BGM.stop()
            game = Cannon()
            running = game.new()
            del(game)
            BGM.play()
        #게임3
        elif running == 6:  
            BGM.stop()
            game = Rhythm()
            running = game.new()
            del(game)
            BGM.play()
        #게임4
        elif running == 7:  
            pass

    pygame.quit()
    sys.exit()

if __name__ == '__main__': main()

    