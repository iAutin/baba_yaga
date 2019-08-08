import pygame, sys


def physics(screen, items_on_screen, screen_dimensions, program_clock):
    
    running = True
    horizontal_velocity = 0
    vertical_velocity = 0
    horizontal_acceleration = 0
    vertical_acceleration = 0
    #[SQLID, Name, Inital Location X, Inital Location y, width, height, button alternate 1, butotn alternate 2]
    #velocity = vel init + accel * time

    while running == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #pygame.key.set_repeat(1,10)
            
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                #pygame.key.name()
                print(pressed_keys)

        for item in items_on_screen:
            item_surface = pygame.transform.scale(pygame.image.load(item[8]),(item[4]*screen_dimensions["width_unit"],item[5]*screen_dimensions["height_unit"]))
            screen.blit(item_surface, (item[2]*screen_dimensions["width_unit"],item[3]*screen_dimensions["height_unit"]))
        
        if items_on_screen[0][2] < 200:
            items_on_screen[0][2] += 1

        pygame.display.flip()
        program_clock.tick(60)

    pygame.display.quit()
    pygame.quit()