import dearpygui.dearpygui as dpg
from Login_UI import render_login_window

def main():
    dpg.create_context()
    dpg.create_viewport(title='Car Rental System Display',x_pos=0, y_pos=0)
    dpg.show_viewport()
    dpg.maximize_viewport()

    render_login_window()

    dpg.setup_dearpygui()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__": 
    main()
