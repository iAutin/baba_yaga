def set_screen_dimensions(width, height):
    width_unit = int(width/200)
    height_unit = int(height/100)
    width_in_units = width * width_unit
    height_in_units = height * height_unit
    screen_dimesions = {"screen_width" : width, "screen_height" : height, "width_unit" : width_unit, "height_unit" : height_unit, "width_in_units": width_in_units, "height_in_units" : height_in_units}
    return screen_dimesions