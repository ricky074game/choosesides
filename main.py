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
cooldown_timer = 100 

# Colors
green = 0, 204, 0
light_green = 20, 217, 72
blue = 0, 0, 204
light_blue = 20, 145, 217
black = 0, 0, 0
white = 255, 255, 255

# Animation
animation_timer = 0
bounce = 0
color_go = 0
animation_start = False
color_animation = 0
already_decided = False
animation_load = False

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

# Save are fun, including using files in order to get those stats
def save(id, option):
    file = open("stats", "r")
    stats = file.readlines()
    file.close()
    file = open("stats", "w+")
    stats[id] = stats[id].strip("\n")
    num = stats[id].split("_")
    if option == 0:
        num[0] = int(num[0]) + 1
    else:
        num[1] = int(num[1]) + 1
    for answer in range(1, 256):
        if id == answer:
            file.write(str(num[0]) + "_" + str(num[1]) + "\n")
        else:
            file.write(stats[id] + "\n")

# Create file filled with info if found blank
file = open("stats", "a+")
test = file.readlines()
file.close()
if test == []:
    file = open("stats", "w+")
    for num in range(256):
        file.write("0_0" + "\n")
    file.close()

# Game Loop
while True:
    clock.tick(60)
    game_timer = game_timer + 1
    screen.fill(black)

# Animation Load Things
    if animation_start and game_timer == animation_timer:
        animation_load = True
    else:
        if animation_start:
            if color_go == 0 and color_animation == 0:
                py.draw.rect(screen, light_green, rect_rectangleleft)
                py.draw.rect(screen, blue, rect_rectangleright)
            if color_go == 0 and color_animation == 1:
                py.draw.rect(screen, green, rect_rectangleleft)
                py.draw.rect(screen, blue, rect_rectangleright)
            if color_go == 1 and color_animation == 0:
                py.draw.rect(screen, green, rect_rectangleleft)
                py.draw.rect(screen, light_blue, rect_rectangleright)
            if color_go == 1 and color_animation == 1:
                py.draw.rect(screen, green, rect_rectangleleft)
                py.draw.rect(screen, light_blue, rect_rectangleright)
# Draw Inital Rectangles
    if animation_start:
        if bounce == 19:
            animation_start = False
        print(bounce)
        if bounce != 19:
            already_decided = False
            if color_go == 0 and color_animation == 1 and not already_decided and animation_load:
                py.draw.rect(screen, light_green, rect_rectangleleft)
                py.draw.rect(screen, blue, rect_rectangleright)
                color_animation = 30 + game_timer
                previous_color = 1
                color_animation = 0
                bounce = bounce + 1
                already_decided = True
            if color_go == 0 and color_animation == 0 and not already_decided and animation_load:
                py.draw.rect(screen, green, rect_rectangleleft)
                py.draw.rect(screen, blue, rect_rectangleright)
                color_animation = 30 + game_timer
                color_animation = 1
                bounce = bounce + 1
                already_decided = True
            if color_go == 1 and color_animation == 1 and not already_decided and animation_load:
                py.draw.rect(screen, green, rect_rectangleleft)
                py.draw.rect(screen, light_blue, rect_rectangleright)
                color_animation = 30 + game_timer
                color_animation = 0
                bounce = bounce + 1
                already_decided = True
            if color_go == 1 and color_animation == 0 and not already_decided and animation_load:
                py.draw.rect(screen, green, rect_rectangleleft)
                py.draw.rect(screen, light_blue, rect_rectangleright)
                color_animation = 30 + game_timer
                color_animation = 0
                bounce = bounce + 1
                already_decided = True
    else:
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
            if text_selected and not player_selected:
                cooldown_timer = game_timer + 30
                if mouse_pos[0] <= 210 and mouse_pos[1] >= 50:
                    save(id_selected, 0)
                    animation_start = True
                    color_go = 0
                    animation_timer = game_timer + 1
                    bounce = 0
                    player_selected = True
                    color_animation = 1
                else:
                    if mouse_pos[0] >= 210 and mouse_pos[1] >= 50:
                        save(id_selected, 1)
                        animation_start = True
                        color_go = 1
                        animation_timer = game_timer + 1
                        bounce = 0
                        player_selected = True
                        color_animation = 1
    

# Draw Text
    screen.blit(title_font, title_font_rect)
    screen.blit(option_1, option1_rect)
    screen.blit(option_2, option2_rect)
    py.display.update()