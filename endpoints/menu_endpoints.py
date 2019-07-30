import sqlite3, sys
from helpful_functions import return_complex_tuple_into_list

#gets all items in menu asset db
def get_menu_items():
    connection = sqlite3.connect("db_generation/menu_assets.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM menu_items")
    menu_items = crsr.fetchall()
    connection.close()
    menu_items = return_complex_tuple_into_list(menu_items)
    return menu_items

#gets all items in test level db
def get_test_level_items():
    connection = sqlite3.connect("db_generation/level_assets.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM test_level_assets")
    test_level_items = crsr.fetchall()
    connection.close()
    test_level_items = return_complex_tuple_into_list(test_level_items)
    return test_level_items

