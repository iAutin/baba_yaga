import sqlite3

def generate_menu_database():
    #generates the menu_assets db
    connection = sqlite3.connect("baba_yaga/db_generation/menu_assets.db")
    crsr = connection.cursor()

    crsr.execute("""CREATE TABLE menu_items ("item_id" Int, "item_name" VARCHAR, "x_pos" Int, "y_pos" Int, "width" Int, "height" Int,"unpressed_id" Int, "pressed_id" Int,"file_location" VARCHAR)""")

    crsr.execute("INSERT INTO menu_items VALUES(?,?,?,?,?,?,?,?,?)", (0,"start_unpressed",80,90,50,10,0,1,"baba_yaga/imgs/menus/main_menu/start_unpressed.png"))
    crsr.execute("INSERT INTO menu_items VALUES(?,?,?,?,?,?,?,?,?)", (1,"start_pressed",80,90,50,10,0,1,"baba_yaga/imgs/menus/main_menu/start_pressed.png"))
    crsr.execute("INSERT INTO menu_items VALUES(?,?,?,?,?,?,?,?,?)", (2,"end_unpressed",140,90,50,10,2,3,"baba_yaga/imgs/menus/main_menu/end_unpressed.png"))
    crsr.execute("INSERT INTO menu_items VALUES(?,?,?,?,?,?,?,?,?)", (3,"end_pressed",140,90,50,10,2,3,"baba_yaga/imgs/menus/main_menu/end_pressed.png"))

    connection.commit()
    print("menu item database created")

    connection.commit()
    connection.close()

def generate_asset_database():
    connection = sqlite3.connect("baba_yaga/db_generation/level_assets.db")
    crsr = connection.cursor()
    
    crsr.execute("""CREATE TABLE test_level_assets ("item_id" Int, "item_name" VARCHAR, "x_pos" Int, "y_pos" Int, "width" Int, "height" Int,"unpressed_id" Int, "pressed_id" Int,"file_location" VARCHAR)""")

    crsr.execute("INSERT INTO test_level_assets VALUES(?,?,?,?,?,?,?,?,?)", (0,"start",10,50,10,10,0,0,"baba_yaga/imgs/test_level/start_portal.png"))
    crsr.execute("INSERT INTO test_level_assets VALUES(?,?,?,?,?,?,?,?,?)", (1,"end",190,50,10,10,1,1,"baba_yaga/imgs/test_level/end_portal.png"))
    crsr.execute("INSERT INTO test_level_assets VALUES(?,?,?,?,?,?,?,?,?)", (2,"unit",0,0,5,5,2,2,"baba_yaga/imgs/test_level/unit.png"))

    connection.commit()
    print("menu item database created")

    connection.commit()
    connection.close()
