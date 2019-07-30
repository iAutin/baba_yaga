import pygame, sys
from endpoints.menu_endpoints import get_menu_items, get_test_level_items

#provides all menu items for screen to be put up
def set_up_menu(screen):
    menu_items = get_menu_items()
    items_on_screen = [menu_items[0],menu_items[2]]
    background = pygame.image.load("imgs/menus/main_menu/baba_yaga_menu_background.png")
    screen.blit(background,(0,0))
    return items_on_screen

#provides all test level items for screen to be put up
def set_up_test_level(screen):
    test_level_items = get_test_level_items()
    items_on_screen = [test_level_items[0],test_level_items[1],test_level_items[2]]
    background = pygame.image.load("imgs/menus/main_menu/baba_yaga_menu_background.png")
    screen.blit(background,(0,0))
    return items_on_screen