import pygame as py
import sys
import random

py.init()
py.display.init()
py.mixer.init()
size = width, height = 420, 360
screen = py.display.set_mode(size)
clock = py.time.Clock()
sound = py.mixer.music.load("sound_test.wav")
time = 0

while True:
    clock.tick(10)
    time = time + 1
    if time == 40:
        py.mixer.music.play(loops=0, start=0.0)
        time = 0
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()