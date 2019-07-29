import pygame, sys, os
from initialize_program import initialize_program
from menu_endpoints import get_menu_items, get_test_level_items

initialize_program()

print("launching pygame")

pygame.init()

program_clock = pygame.time.Clock()

screen_width = 1366
width_unit = int(screen_width/200)
screen_height = 768
height_unit = int(screen_height/100)

pygame.display.init()
screen = pygame.display.set_mode([screen_width,screen_height])

running = True
time = 0

current_page = "test_level"
items_on_screen = []

movement_x = 0
movement_y = 0
while (running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_xy = pygame.mouse.get_pos()
        
        if event.type == pygame.KEYDOWN:
            pressed_list = pygame.key.get_pressed()
            if pressed_list [119] == 1:
                print("w")
                movement_y = movement_y - 2
            if pressed_list [97] == 1:
                print("a") 
                movement_x = movement_x - 2
            if pressed_list [115] == 1:
                print("s")
                movement_y = 5 + movement_y
            if pressed_list [100] == 1:
                print("d")
                movement_x = 5 + movement_x


    if (current_page == "menu"):
        menu_items = get_menu_items()
        background = pygame.image.load("baba_yaga/imgs/menus/main_menu/baba_yaga_menu_background.png")
        items_on_screen.append(menu_items[0])
        items_on_screen.append(menu_items[2])
    
    if (current_page == "test_level"):
        test_level_items = get_test_level_items()
        background = pygame.image.load("baba_yaga/imgs/menus/main_menu/baba_yaga_menu_background.png")
        items_on_screen = []
        items_on_screen.append(test_level_items[0])
        items_on_screen.append(test_level_items[1])
        items_on_screen.append(test_level_items[2])

    screen.blit(background,(0,0))

    for item in items_on_screen:

        item_surface = pygame.transform.scale(pygame.image.load(item[8]),(item[4]*width_unit,item[5]*height_unit))
        screen.blit(item_surface, (item[2]*width_unit+(movement_x*width_unit),item[3]*height_unit+(movement_y*height_unit)))

    pygame.display.flip()

program_clock.tick(60)

print("quiting pygame")
pygame.display.quit()
pygame.quit()
print("pygame ended")