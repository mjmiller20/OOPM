import dearpygui.dearpygui as dpg
from Current_Upcoming_Reservation_UI import render_reservation_window

login_window = ""
top_window = ""

def login_callback(sender, app_data, user_data):
    print("Username = " + dpg.get_value("Username_text"))
    print("Password = " + dpg.get_value("Password_text"))

    dpg.delete_item(login_window)
    dpg.delete_item(top_window)

    render_reservation_window()

def new_user_callback(sender, app_data, user_data):
    print("new_user")

def render_login_window():
    global login_window
    global top_window
    #set theme for text
    with dpg.theme(tag="text_theme1"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (22, 12, 110))

    #set theme for window
    with dpg.theme(tag="__win_theme1"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (173, 216, 250))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (173, 216, 250))
                
    with dpg.theme(tag="topWin_theme1"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255,255,255))


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

    with dpg.theme(tag="input_text_theme"):
        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (22, 12, 110))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255))

    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()

    with dpg.font_registry():
        #default_font=dpg.add_font("Quicksand-VariableFont_wght.ttf", h*.028)
        Res_font=dpg.add_font("Arial.otf", h*.030)
        title_font=dpg.add_font("Arial.otf", h*.05)
        #third_font
        
    with dpg.texture_registry():
        width, height, channels, data=dpg.load_image("CarRentalLogo.png")
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="CarRentalLogo")
        width, height, channels, data=dpg.load_image("ProfileLogo.png")
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="ProfileLogo")
        
    #create top bar
    with dpg.window(label="Car Rental System", no_close=True, no_collapse=True, no_resize=True, no_move=True) as loginWin:
        dpg.bind_item_theme(loginWin, "__win_theme")
        with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, min_size=(0,0), width=w, height=h*.083, pos=(0,0)) as topWin:
            dpg.add_image_button(texture_tag="CarRentalLogo", label="Car Rental System", pos=(0,0), width=h*.1, height=h*.075)
            dpg.add_text("Car Rental System", pos=(h*.11,h*.020))
            dpg.bind_item_font(dpg.last_item(), title_font)
            
        dpg.add_text("Welcome!", pos=(w*.44, h*.25))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), title_font)

        dpg.add_text("Please Log in using your Username and Password", pos=(w*.22, h*.30))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), title_font)


        dpg.add_text("Username: ", pos=(w*.05, h*.45))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), title_font)

        dpg.add_input_text(tag="Username_text", pos=(w*.2, h*.45), width=w*.65, height=h*.075)
        dpg.bind_item_theme(dpg.last_item(), "input_text_theme")
        dpg.bind_item_font(dpg.last_item(), title_font)

        dpg.add_text(" Password: ", pos=(w*.05, h*.55)) 
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), title_font)

        dpg.add_input_text(tag="Password_text", pos=(w*.2, h*.55), width=w*.65, height=h*.15, password=True)
        dpg.bind_item_theme(dpg.last_item(), "input_text_theme")
        dpg.bind_item_font(dpg.last_item(), title_font)

        #Login button             
        dpg.add_button(label="Login", pos=(w*.35, h*.70), width=w*.3, height=h*.075, callback=login_callback)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), title_font)

        #new user text             
        dpg.add_button(tag="new_user", label="New User? Create an Account",  pos=(w*.35, h*.80), width=w*.3, height=h*.075, callback=new_user_callback)
        dpg.bind_item_theme(dpg.last_item(), "new_user_button")
        dpg.bind_item_font(dpg.last_item(), Res_font)
        
    dpg.bind_item_theme(loginWin, "__win_theme1")
    dpg.bind_item_theme(topWin, "topWin_theme1")

    dpg.set_primary_window(loginWin, True)

    login_window = loginWin
    top_window = topWin

