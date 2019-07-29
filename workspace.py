import pygame, sys, os

print("launching pygame")
pygame.init()

program_clock = pygame.time.Clock()

screen_width = 1366
screen_height = 768

pygame.display.init()
screen = pygame.display.set_mode([screen_width,screen_height])

running = True
time = 0
background = pygame.image.load("baba_yaga/imgs/menus/main_menu/baba_yaga_menu_background.png")

current_page = "menu"
items_on_screen = []
while (running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_pos()
            
    if current_page == "menu":

        start_button = {
        "name" : "start_button", 
        "x_pos" : 500,
        "y_pos" : 600,
        "file_location" : "baba_yaga/imgs/menus/main_menu/start_unpressed.png"
        }
        quit_button = {
        "name" : "quit_button", 
        "x_pos" : 900,
        "y_pos" : 600,
        "file_location" : "baba_yaga/imgs/menus/main_menu/end_unpressed.png"
        }

        items_on_screen.append(start_button)
        items_on_screen.append(quit_button)



    screen.blit(background,(0,0))

    for item in items_on_screen:

        item_surface = pygame.image.load(item["file_location"])
        screen.blit(item_surface, (item["x_pos"],item["y_pos"]))

    pygame.display.flip()

program_clock.tick(60)

print("quiting pygame")
pygame.display.quit()
pygame.quit()
print("pygame ended")