import dearpygui.dearpygui as dpg

def visual_registry(h):
    '''fonts'''
    with dpg.font_registry():
        dpg.add_font(tag="Res_font", file="Arial.otf", size=h*.030)
        dpg.add_font(tag="title_font", file="Arial.otf", size=h*.05)

    '''themes'''
    #text themes
    with dpg.theme(tag="Text_Button_align_right"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 1, .5)
            
    with dpg.theme(tag="text_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0,0,255))
            
    with dpg.theme(tag="text_theme1"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (22, 12, 110))
    
    #input box themes
    with dpg.theme(tag="input_box_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (175, 175, 175))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255))
    
    with dpg.theme(tag="input_text_theme"):
        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (22, 12, 110))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255))
    
    #drop down themes
    with dpg.theme(tag="dropdown_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (175, 175, 175))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255))
    
    #window themes        
    with dpg.theme(tag="__win_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (173, 216, 250))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (173, 216, 250))
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (203, 229, 250))
                
    with dpg.theme(tag="topWin_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255,255,255))
    
    #button themes
    with dpg.theme(tag="Login_button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (208,242,252))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (208,242,252))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (188,222,242))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (22, 12, 110))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,5)

    with dpg.theme(tag="new_user_button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (173, 216, 250))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (208,242,252))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (173, 216, 250))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (22, 12, 110))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,5)
            
    with dpg.theme(tag="Reservation_button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (250,250,250))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (250,250,250))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (211,211,211))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0,0,255))
            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, .02, .5)

    with dpg.theme(tag="NewReservation_button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (208,242,252))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (208,242,252))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (188,222,242))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0,0,255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,5)
                
    with dpg.theme(tag="Availability_Button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (250,250,250))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (250,250,250))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (211,211,211))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0,0,255))
            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, .02, .5)
    
    with dpg.theme(tag="Show_Availability_Button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (208,242,252))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (208,242,252))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (188,222,242))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0,0,255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,5)
            
    '''textures'''       
    with dpg.texture_registry():
        width, height, channels, data=dpg.load_image("CarRentalLogo.png")
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="CarRentalLogo")
        width, height, channels, data=dpg.load_image("ProfileLogo.png")
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="ProfileLogo")
    