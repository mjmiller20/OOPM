import dearpygui.dearpygui as dpg

def add_fonts(h):
    with dpg.font_registry():
        dpg.add_font(tag="Res_font", file="Arial.otf", size=h*.030)
        dpg.add_font(tag="title_font", file="Arial.otf", size=h*.05)

