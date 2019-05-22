# import random,os,sys,math #socket
# import pygame as pg
from script import *

from script.tiled_lvl import Tiled, SPACEMAP, lvl_map
from script.mission import Mission
from script.interface import Interface



class Game:

    def __init__(self, SURFACE,lvl):
        self.player = None
        self.player_2=None
        self.load()

        # Map
        self.lvl_map = lvl_map
        SPACEMAP = 42

        # Temp
        self.lvl = lvl
        self.tile = Tiled(self.lvl_map[self.lvl], self)
        self.mission = Mission(self)

        # Surface
        self.surface = SURFACE
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        self.tile_image = self.tile.make_map(self.lvl_map[self.lvl],SPACEMAP)



    def load(self):
        # __GROUP__#

        self.bullets = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.sprites = pg.sprite.Group()
        self.obs = pg.sprite.Group()
        self.objs = pg.sprite.Group()
        self.effect = pg.sprite.Group()

    def start(self, SURFACE, WIDTH, HEIGHT):
        self.surface = SURFACE
        self.image = image["lvl"]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = HEIGHT
        self.rect.x, y = WIDTH, HEIGHT
        SURFACE.blit(self.image, self.rect)

    def update(self):
        self.enemies.update()
        self.sprites.update()
        self.objs.update()
        self.bullets.update()
        self.mission.update()
        self.effect.update()

        self.draw()

    def draw(self):
        self.surface.blit(self.tile_image, (0, 0))
        self.bullets.draw(self.surface)
        self.objs.draw(self.surface)
        self.enemies.draw(self.surface)
        self.effect.draw(self.surface)
        self.sprites.draw(self.surface)


def loop():

    map_tmp = lvl_map[lvl]

    WIDTH = len(map_tmp[0]) * SPACEMAP
    HEIGHT = len(map_tmp) * SPACEMAP

    SCREEN = pg.display.set_mode((WIDTH, HEIGHT + 42))
    SURFACE = pg.Surface((WIDTH, HEIGHT))
    pg.display.set_caption(" Tank ")

    exit = False
    clock = pg.time.Clock()
    game = Game(SURFACE,  lvl)
    interface = Interface(game)

    while exit != True :

        clock.tick(70)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit = True
                if event.key == pg.K_KP_ENTER:
                    if game.player_2.cannon.load == True:
                        game.player_2.cannon.fire = True
                elif event.key == pg.K_LEFT:
                    game.player_2.rotate(1)
                    game.player_2.move_bool = 1
                elif event.key == pg.K_RIGHT:
                    game.player_2.rotate(-1)
                    game.player_2.move_bool = 1
                elif event.key == pg.K_UP:
                    game.player_2.rotate(2)
                    game.player_2.move_bool = 1
                elif event.key == pg.K_DOWN:
                    game.player_2.rotate(-2)
                    game.player_2.move_bool = 1

                if event.key == pg.K_SPACE:
                    if game.player.cannon.load == True:
                        game.player.cannon.fire = True
                if event.key == pg.K_a:
                    game.player.rotate(1)
                    game.player.move_bool = 1
                elif event.key == pg.K_d:
                    game.player.rotate(-1)
                    game.player.move_bool = 1
                elif event.key == pg.K_w:
                    game.player.rotate(2)
                    game.player.move_bool = 1
                elif event.key == pg.K_s:
                    game.player.rotate(-2)
                    game.player.move_bool = 1

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    game.player_2.move_bool = 0
                elif event.key == pg.K_DOWN:
                    game.player_2.move_bool = 0
                elif event.key == pg.K_LEFT:
                    game.player_2.move_bool = 0
                elif event.key == pg.K_RIGHT:
                    game.player_2.move_bool = 0


                if event.key == pg.K_w:
                    game.player.move_bool = 0
                elif event.key == pg.K_s:
                    game.player.move_bool = 0
                elif event.key == pg.K_a:
                    game.player.move_bool = 0
                elif event.key == pg.K_d:
                    game.player.move_bool = 0

        if  game.player.vidas==0 :
                game = Game(SURFACE, "v1")
                game.update()
                SCREEN.blit(SURFACE, (0, 0))
                pg.display.flip()
                while True:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            exit(0)
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                exit(0)

        elif game.player_2.vidas==0:
                game = Game(SURFACE, "v2")
                game.update()
                SCREEN.blit(SURFACE, (0, 0))
                pg.display.flip()
                while True:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            exit(0)

                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                exit(0)
        else:

            game.update()
            SCREEN.blit(SURFACE, (0, 0))
            interface.update()
            interface.draw(SCREEN)
            pg.display.flip()



if __name__ == "__main__":


    pg.init()

    width = 966
    height = 588

    screen = pg.display.set_mode((width, height))


    pg.display.flip()
    dog_surf = pg.image.load("image/lvl.png")
    dog_rect = dog_surf.get_rect(bottomright=(966, 588))
    screen.blit(dog_surf, dog_rect)

    pg.display.update()
    lvl_number=0
    """
    while lvl_number==-1:
        for event in pg.event.get():
            z = list(pg.mouse.get_pressed())
            print(z[1])
            if (z[0] > 109 and z[1]>209) and (z[0]<380 and z[1]<320):
                lvl_number = 0
            elif (z[0]>460 and z[1]>209) and (z[0]<730 and z[1]<320):
                lvl_number = 1


    try:
        lvl_number = int(input('Введите номер уровня (0/1) '))
    except:
        print('Вы ввели неправильное значение')"""
    lvl = "lvl_" + str(lvl_number)
    loop()
    pg.quit()
