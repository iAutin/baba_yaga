import sqlite3
from db_generation.db_generation import generate_menu_database

def clear_databases():
    #Deletes all db tables in the try.
    connection = sqlite3.connect("baba_yaga/db_generation/menu_assets.db")
    crsr = connection.cursor()
    try:
        crsr.execute("""DROP TABLE menu_items""")
    except:
        print("menu_items tables does not currently exist in menu assets db")
    connection.commit()
    connection.close()

def create_databases():
    #generates all necessary tables
    generate_menu_database()

def initialize_program():
    #clears and then generates all db tables
    clear_databases()
    create_databases()