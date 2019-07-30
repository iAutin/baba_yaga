import sqlite3, pygame, sys
from helpful_functions import return_complex_tuple_into_list

def get_menu_items():
    connection = sqlite3.connect("db_generation/menu_assets.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM menu_items")
    menu_items = crsr.fetchall()
    connection.close()
    menu_items = return_complex_tuple_into_list(menu_items)
    return menu_items

def get_test_level_items():
    connection = sqlite3.connect("db_generation/level_assets.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM test_level_assets")
    menu_items = crsr.fetchall()
    connection.close()
    menu_items = return_complex_tuple_into_list(menu_items)
    return menu_items

def set_up_menu(screen):
    menu_items = get_menu_items()
    items_on_screen = [menu_items[0],menu_items[2]]
    background = pygame.image.load("imgs/menus/main_menu/baba_yaga_menu_background.png")
    screen.blit(background,(0,0))
    return items_on_screen

def set_up_test_level(screen):
    test_level_items = get_test_level_items()
    items_on_screen = [test_level_items[0],test_level_items[1],test_level_items[2]]
    background = pygame.image.load("imgs/menus/main_menu/baba_yaga_menu_background.png")
    screen.blit(background,(0,0))
    return items_on_screen