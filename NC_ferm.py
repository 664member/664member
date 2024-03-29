import pyautogui as pg
import sys
import msvcrt
import random

import os
import signal
import keyboard
import multiprocessing


def hook(pid):
    while True:
        if keyboard.is_pressed('esc'):
            os.kill(pid,signal.SIGTERM)
            os._exit(1)


if __name__ == '__main__':
    pid = os.getpid()
    multiprocessing.Process(target=hook,args=[pid]).start()
    print('Press Ctrl-C to quit.')
    startX = 960
    startY = 720
    clickerSpeed = 0.0005
    startX = 960
    startY = 720
    clickerSpeed = 0.65
    try:
        X = pg.prompt('Enter','startX', startX)
        Y = pg.prompt('Enter','startY', startY)
        sp = pg.prompt('Enter','clickerSpeed', clickerSpeed)
        if(X is not None and isinstance(X, (int, float,str))):
            startX = int(X)
        if(Y is not None and isinstance(Y, (int, float, str))):
            startY = int(Y)
        if(sp is not None and isinstance(sp, (int, float, str))):
            clickerSpeed = float(sp)        
        while(True):
            if(pg.position().x > startX + 50 or pg.position().x < startX-50 or pg.position().y > startY+10 or pg.position().y < startY-50):
                pg.moveTo(startX,startY, clickerSpeed, pg.easeOutQuad)
            pg.move(random.randint(1,20)-random.randint(1,20) , random.randint(1,10)-random.randint(1,10),clickerSpeed)
            pg.click(clicks=2, interval = clickerSpeed)
            if(msvcrt.kbhit()):
                break
    except KeyboardInterrupt:
        print('\n') 




