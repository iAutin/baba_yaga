import pygame, sys, os
from initialize_program import initialize_program
from functions.menu_functions import set_up_menu, set_up_test_level
from endpoints.menu_endpoints import get_menu_items, get_test_level_items
from functions.screen_functions import set_screen_dimensions
from functions.clicking_checks import check_for_click
from functions.physics_functions import physics

initialize_program()
pygame.init()
program_clock = pygame.time.Clock()

#screen dimensions {"screen_width", "screen_height", "width_unit", "height_unit", "width_in_units", "height_in_units"}
screen_dimensions = set_screen_dimensions(1366,768)
pygame.display.init()
screen = pygame.display.set_mode((screen_dimensions["screen_width"], screen_dimensions["screen_height"]))
running = True
current_page = "test_level"
initialized_page = False
items_on_screen = []

while (running == True):
    #start of idle loop
    clicked_down = 0
    clicked_up = 0
    clicked_up_bool = False
    #event queue listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_xy = pygame.mouse.get_pos()
            clicked_down = check_for_click(mouse_xy, items_on_screen, screen_dimensions)

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_xy = pygame.mouse.get_pos()
            clicked_up = check_for_click(mouse_xy, items_on_screen, screen_dimensions)
            clicked_up_bool = True
        
    #page interpreter
    if (current_page == "menu") and initialized_page == False:
        all_menu_items = get_menu_items()
        items_on_screen = set_up_menu(screen, all_menu_items)
        initialized_page = True

    if (current_page == "menu") and initialized_page == True:
        if clicked_down != 0:
            for i, item in enumerate(items_on_screen):
                if clicked_down == item:
                    items_on_screen[i] = all_menu_items[item[7]]
        clicked_down = 0

        if clicked_up_bool == True:
            for i, item in enumerate(items_on_screen):
                if item[1] != item[6]:
                    items_on_screen[i] = all_menu_items[item[6]]
        if clicked_up != 0:
            if ((clicked_up[1] == "start_pressed") or (clicked_up[1] == "start_unpressed")):
                initialized_page = False
                current_page = "test_level"
            elif ((clicked_up[1] == "end_pressed") or (clicked_up[1] == "end_unpressed")):
                running = False
        clicked_up = 0

    if (current_page == "test_level") and initialized_page == False:
        all_test_level_items = get_test_level_items()
        items_on_screen = set_up_test_level(screen, all_test_level_items)
        initalized_page = True

        physics(screen, items_on_screen, screen_dimensions, program_clock)



    #screen updater
    #[SQLID, Name, Inital Location X, Inital Location y, width, height, button alternate 1, butotn alternate 2]
    for item in items_on_screen:
        item_surface = pygame.transform.scale(pygame.image.load(item[8]),(item[4]*screen_dimensions["width_unit"],item[5]*screen_dimensions["height_unit"]))
        screen.blit(item_surface, (item[2]*screen_dimensions["width_unit"],item[3]*screen_dimensions["height_unit"]))


    pygame.display.flip()
    
    program_clock.tick(60)

pygame.display.quit()
pygame.quit()