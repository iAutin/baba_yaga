import pygame, sys, os
from initialize_program import initialize_program
from menu_endpoints import get_test_level_items, set_up_menu, set_up_test_level
from screen_endpoints import set_screen_dimensions

initialize_program()
pygame.init()
program_clock = pygame.time.Clock()

screen_dimensions = set_screen_dimensions(1366,768)
pygame.display.init()
screen = pygame.display.set_mode((screen_dimensions["screen_width"], screen_dimensions["screen_height"]))

running = True

current_page = "menu"
items_on_screen = []

movement_x = 0
movement_y = 0
while (running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_xy = pygame.mouse.get_pos()
  
    if (current_page == "menu"):
        items_on_screen = set_up_menu(screen)
        
    if (current_page == "test_level"):
        items_on_screen = get_test_level_items(screen)

    for item in items_on_screen:
        item_surface = pygame.transform.scale(pygame.image.load(item[8]),(item[4]*screen_dimensions["width_unit"],item[5]*screen_dimensions["height_unit"]))
        screen.blit(item_surface, (item[2]*screen_dimensions["width_unit"],item[3]*screen_dimensions["height_unit"]))

    pygame.display.flip()
    
program_clock.tick(60)

print("quiting pygame")
pygame.display.quit()
pygame.quit()
print("pygame ended")