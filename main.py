import pygame as py
import sys
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
cooldown_timer = 100 
already_selected_option = False

# Set inital sprites
rect_rectangleleft = py.Rect(0, 50, 210, 310)
rect_rectangleright = py.Rect(210, 50, 210, 310)
normal_font = py.font.SysFont("a", 20, True, False)
title_font = py.font.Font.render(normal_font, "Would you rather is loading...", False, white)
title_font_rect = title_font.get_rect()
title_font_rect = title_font_rect.move(110, 20)
option_1 = py.font.Font.render(normal_font, "", True, black)
option_2 = py.font.Font.render(normal_font, "", True, black)
option1_rect = option_1.get_rect()
option2_rect = option_2.get_rect()

# Get Text Loop for each ID
def get_text(id, require):
    if require == 1:
        title_font_text = "Would you rather?"
        return title_font_text
    if id == 1:
        if require == 2:
            option1_text = "Be a human"
            return option1_text
        if require == 3:
            option2_text = "Be a human"
            return option2_text
def get_stats(id, option):
    open("stats", "w")



# Game Loop
while True:
    clock.tick(60)
    game_timer = game_timer + 1
    screen.fill(black)

# Draw Inital Rectangles
    py.draw.rect(screen, green, rect_rectangleleft)
    py.draw.rect(screen, blue, rect_rectangleright)
    if game_timer == 60:
        player_decision = True
        text_selected = False

# Exit game

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

# Gets text, if player decision and text is not chosen

    if not text_selected and player_decision:
        id_selected = random.randint(1 , 1)
        title_font = py.font.Font.render(normal_font, get_text(id_selected, 1), True, white)
        option_1 = py.font.Font.render(normal_font, get_text(id_selected, 2), True, black)
        option_2 = py.font.Font.render(normal_font, get_text(id_selected, 3), True, black)
        title_font_rect = title_font.get_rect()
        title_font_rect = title_font_rect.move(150, 20)
        option1_rect = option_1.get_rect()
        option2_rect = option_2.get_rect()
        option1_rect = option1_rect.move(70, 180)
        option2_rect = option2_rect.move(270, 180)
        text_selected = True
        player_selected = False
    
# Start mouse controls
    mouse_pos = py.mouse.get_pos()
    button = py.mouse.get_pressed(3)

# Get Mouse Button if Pressed
    if button == (True, False, False) or button == (True, False, True):
        if cooldown_timer <= game_timer:
            if text_selected and not player_selected and not already_selected_option:
                cooldown_timer = game_timer + 30
                if mouse_pos[0] <= 210 and mouse_pos[1] >= 50:
                    print("Option 1")
                else:
                    if mouse_pos[0] >= 210 and mouse_pos[1] >= 50:
                        print("Option 2")

# Draw Text
    screen.blit(title_font, title_font_rect)
    screen.blit(option_1, option1_rect)
    screen.blit(option_2, option2_rect)
    py.display.update()