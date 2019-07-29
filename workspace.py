import pygame, sys, os
from initialize_program import initialize_program
from menu_endpoints import get_menu_items

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

current_page = "menu"
items_on_screen = []


while (running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_pos()
    if (current_page == "menu"):
        menu_items = get_menu_items()
        background = pygame.image.load("baba_yaga/imgs/menus/main_menu/baba_yaga_menu_background.png")
        items_on_screen.append(menu_items[0])
        items_on_screen.append(menu_items[2])
        
    screen.blit(background,(0,0))
    for item in items_on_screen:

        item_surface = pygame.image.load(item[8])
        screen.blit(item_surface, (item[2]*width_unit,item[3]*height_unit))

    pygame.display.flip()

program_clock.tick(60)

print("quiting pygame")
pygame.display.quit()
pygame.quit()
print("pygame ended")