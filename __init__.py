import pygame as pg
import os.path
import pygame as pg

pg.display.init()
pg.joystick.init()
pg.font.init()

resolve_route = lambda route_relative: os.path.join(os.path.abspath("."), route_relative)

pg.mixer.init()

import math

image = {
    "tank_0": pg.image.load(resolve_route("image/limonero_tank.png")),
    "tank_0_gun": pg.image.load(resolve_route("image/limonero_gun.png")),
    "tank_1": pg.image.load(resolve_route("image/uvadero_tank.png")),
    "tank_1_gun": pg.image.load(resolve_route("image/uvadero_gun.png")),
    "bullet_1": pg.image.load(resolve_route("image/bullet_a.png")),
    "bullet_0": pg.image.load(resolve_route("image/bullet_lvl2.png")),
    "rect": pg.image.load(resolve_route("image/Rect.png")),
    "box": pg.image.load(resolve_route("image/box.png")),
    "gun": pg.image.load(resolve_route("image/gun2x.png")),
    "wave_shot": pg.image.load("image/effect_shot.png"),
    "explosion": pg.image.load("image/effect_explosion.png"),
    "lvl":pg.image.load("image/lvl.png")
}
sound = {
			"shot": pg.mixer.Sound(resolve_route("sound/shot.wav")),
			"box": pg.mixer.Sound(resolve_route("sound/box.wav")),
			"boomsnd": pg.mixer.Sound(resolve_route("sound/boomsnd.wav")),
			}

