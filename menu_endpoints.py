import sqlite3
from helpful_functions import return_complex_tuple_into_list

def get_menu_items():
    connection = sqlite3.connect("baba_yaga/db_generation/menu_assets.db")
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM menu_items")
    menu_items = crsr.fetchall()
    connection.close()
    menu_items = return_complex_tuple_into_list(menu_items)
    
    return menu_items