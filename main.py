import pygame as py
import sys
import id
import random

# Initialize and set title bar
py.init()
py.display.init()
size = width, height = 420, 360
screen = py.display.set_mode(size)
clock = py.time.Clock()
py.display.set_caption("Would you Rather?")

# Inital Starting Variables
game_state = 1
game_timer = 0
game_settime = 0
player_decision = True
text_selected = True
green = 0, 204, 0
blue = 0, 0, 204
black = 0, 0, 0
white = 255, 255, 255

# Set inital sprites
rect_rectangleleft = py.Rect(0, 50, 210, 310)
rect_rectangleright = py.Rect(210, 50, 210, 310)
normal_font = py.font.SysFont("a", 20, True, False)
title_font = py.font.Font.render(normal_font, "Would you rather is loading...", False, white)
title_font_rect = title_font.get_rect()
title_font_rect = title_font_rect.move(110, 20)

# Game Loop
while True:
    clock.tick(60)
    game_timer = game_timer + 1
    screen.fill(black)
# Draw Inital Rectangles
    py.draw.rect(screen, green, rect_rectangleleft)
    py.draw.rect(screen, blue, rect_rectangleright)
    if game_timer == 10:
        player_decision = False
# Exit game
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
# Gets text, if player decision and text is not chosen
    if not text_selected and player_decision:
        id_selected = random.randint(1 , 2)
        id.get_text(id_selected)
        title_font_rect = title_font.get_rect
        option1_rect = option1.get_rect
        option2_rect = option2.get_rect
# Draw Text
    screen.blit(title_font, title_font_rect)
    py.display.update()