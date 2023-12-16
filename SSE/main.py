import dearpygui.dearpygui as dpg
import dbaccess as dbaccess
from psycopg2 import Error as psycopgError
from Login_UI import render_login_window
from Visual_Registry import visual_registry

def main():
    try:
        dbaccess.DBAccess()

    except (Exception, psycopgError) as error:
        print("Error while connecting to PostgreSQL: ", error) 
        exit()

    dpg.create_context()
    dpg.create_viewport(title='Car Rental System Display',x_pos=0, y_pos=0)
    dpg.show_viewport()
    dpg.maximize_viewport()
    
    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()
    visual_registry(w, h)

    render_login_window()

    dpg.setup_dearpygui()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__": 
    main()
