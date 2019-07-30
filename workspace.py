import pygame, sys, os
from initialize_program import initialize_program
from functions.menu_functions import set_up_menu, get_test_level_items
from functions.screen_functions import set_screen_dimensions
from functions.clicking_checks import check_for_click

initialize_program()
pygame.init()
program_clock = pygame.time.Clock()

#screen dimensions {"screen_width", "screen_height", "width_unit", "height_unit", "width_in_units", "height_in_units"}
screen_dimensions = set_screen_dimensions(1366,768)
pygame.display.init()
screen = pygame.display.set_mode((screen_dimensions["screen_width"], screen_dimensions["screen_height"]))
running = True
current_page = "menu"
items_on_screen = []

while (running == True):
    #event queue listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_xy = pygame.mouse.get_pos()
            check_for_click(mouse_xy, items_on_screen, screen_dimensions)
    #page interpreter
    if (current_page == "menu"):
        items_on_screen = set_up_menu(screen)
        
    if (current_page == "test_level"):
        items_on_screen = get_test_level_items(screen)
    
    #screen updater
    #[SQLID, Name, Inital Location X, Inital Location y, width, height, button alternate 1, butotn alternate 2]
    for item in items_on_screen:
        item_surface = pygame.transform.scale(pygame.image.load(item[8]),(item[4]*screen_dimensions["width_unit"],item[5]*screen_dimensions["height_unit"]))
        screen.blit(item_surface, (item[2]*screen_dimensions["width_unit"],item[3]*screen_dimensions["height_unit"]))

    pygame.display.flip()
    
    program_clock.tick(60)

pygame.display.quit()
pygame.quit()