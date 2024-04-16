import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2= pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")#練習2
    kk_img = pg.transform.flip(kk_img,True,False)#反転
    kk_rct = kk_img.get_rect()#練習8-1
    kk_rct.center=300,200
    kk_dx=0
    kk_dy=0
    tmr = 0
    kk_x = 0

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            kk_dy=-1
        if key_list[pg.K_DOWN]:
            kk_dy=1
        if key_list[pg.K_LEFT]:
            kk_dx=-1
        if key_list[pg.K_RIGHT]:
            kk_dx=2

        x=tmr%3200
        screen.blit(bg_img, [-x, 0])#練習6
        screen.blit(bg_img2,[-x+1600,0])#練習7-1
        screen.blit(bg_img, [-x+3200, 0])#練習6
        screen.blit(bg_img2,[-x+4800,0])#練習7-2
        screen.blit(kk_img,kk_rct.center)#練習7-2
        pg.display.update()
        tmr += 1   
        kk_rct.move_ip((-1+kk_dx,kk_dy))
        kk_dx=0
        kk_dy=0
        clock.tick(200)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()