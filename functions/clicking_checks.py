import pygame, sys

#mouse_xy (tuple) (x,y)
#items_on_screen [SQLID, Name, Inital Location X, Inital Location y, width, height, button alternate 1, butotn alternate 2]
#screen dimensions {"screen_width", "screen_height", "width_unit", "height_unit", "width_in_units", "height_in_units"}

def check_for_click(mouse_xy, items_on_screen, screen_dimensions):
    for item in items_on_screen:
        if (mouse_xy[0] > item[2]*screen_dimensions["width_unit"]) and (mouse_xy[1] > item[3]*screen_dimensions["height_unit"]) and (mouse_xy[0] < (item[2]+item[4])*screen_dimensions["width_unit"]) and (mouse_xy[1] < (item[3]+item[5])*screen_dimensions["height_unit"]):
            return item
    
    return 0