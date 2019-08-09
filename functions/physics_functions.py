import pygame, sys


def physics(screen, items_on_screen, screen_dimensions, program_clock):
    
    running = True
    horizontal_velocity = 0
    vertical_velocity = 0
    horizontal_acceleration = 0
    vertical_acceleration = 0
    #item_on_screen
    #[SQLID, Name, Inital Location X, Inital Location y, width, height, button alternate 1, butotn alternate 2]
    #velocity = vel init + accel * time
    #screen_dimesions = {
    # "screen_width" : width,
    #  "screen_height" : height,
    #  "width_unit" : width_unit,
    #  "height_unit" : height_unit,
    #  "width_in_units": width_in_units,
    #  "height_in_units" : height_in_units}

    #keys
    #a = 97 w = 119 s = 115 d = 100

    while running == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[97] == 1:
                    print("a")
                    horizontal_acceleration = horizontal_acceleration - 3
                if pressed_keys[119] == 1:
                    print("w")
                    vertical_acceleration = vertical_acceleration - 3
                if pressed_keys[115] == 1:
                    print("s")
                    vertical_acceleration = vertical_acceleration + 3
                if pressed_keys[100] == 1:
                    print("d")
                    horizontal_acceleration = horizontal_acceleration + 3
        
        #updates all items on the screen each loop
        for item in items_on_screen:
            if item[1] == 'start':
                item_surface = pygame.transform.scale(pygame.image.load(item[8]),(item[4]*screen_dimensions["width_unit"],item[5]*screen_dimensions["height_unit"]))
                screen.blit(item_surface, (item[2]*screen_dimensions["width_unit"]+horizontal_velocity,item[3]*screen_dimensions["height_unit"]+vertical_velocity))
            else:
                item_surface = pygame.transform.scale(pygame.image.load(item[8]),(item[4]*screen_dimensions["width_unit"],item[5]*screen_dimensions["height_unit"]))
                screen.blit(item_surface, (item[2]*screen_dimensions["width_unit"],item[3]*screen_dimensions["height_unit"]))

        pygame.display.flip()
    pygame.display.quit()
    pygame.quit()