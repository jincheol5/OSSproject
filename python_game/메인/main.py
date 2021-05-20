import pygame
import sys
import os

from settings import *
from start import *
from login import *




def main():
    running = 1
    while running:
        if running == 1:
            s = Start()
            running = s.new()
        elif running == 2:
            l = Login()
            running = l.new()
        elif running == 3:  
            pass
        elif running == 4:  
            pass
        elif running == 5:  
            pass

    pygame.quit()
    sys.exit()

if __name__ == '__main__': main()

    
