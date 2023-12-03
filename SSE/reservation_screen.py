import dearpygui.dearpygui as dpg

dpg.create_context()

name="John Doe"
num_rentals=5

##Themes
##Button Themes
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


##Text Themes
with dpg.theme(tag="Text_Button_align_right"):
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 1, 0.5)

with dpg.theme(tag="text_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 255))

with dpg.theme(tag="input_box_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (175, 175, 175))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255))

with dpg.theme(tag="dropdown_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (175, 175, 175))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 255, 255))


##Window Themes
with dpg.theme(tag="__win_theme"):
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (173, 216, 250))
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (173, 216, 250))

with dpg.theme(tag="topWin_theme"):
    with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (20, 75, 150))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255))


##Button Functions
def get_availability(sender, app_data, user_data):
    num_rentals=5
    print(user_data)

def profile(sender, app_data, user_data):
    print("loading user profile")

def make_and_model(sender, app_data, user_data):
    print(user_data)

def location(sender, app_data, user_data):
    print(user_data)

def see_availability(sender, app_data, user_data):
    num_rentals=5
    dpg.render_dearpygui_frame()    #? Need a way to update gui after something happens
    print(user_data)

##Viewport Setup
dpg.create_viewport(title='Car Rental System Display', x_pos=0, y_pos=0)
dpg.show_viewport()

dpg.maximize_viewport()

w=dpg.get_viewport_width()
h=dpg.get_viewport_height()

##Fonts
with dpg.font_registry():
    Res_font=dpg.add_font("Arial.otf", h*0.030)
    title_font=dpg.add_font("Arial.otf", h*0.05)

with dpg.texture_registry():
    width, height, channels, data=dpg.load_image("CarRentalLogo.png")
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="CarRentalLogo")
    width, height, channels, data=dpg.load_image("ProfileLogo.png")
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="ProfileLogo")

#Main Window
with dpg.window(label="Car Rental System", no_close=True, no_collapse=True, no_resize=True, no_move=True) as mainWin:

    ##Header
    with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, min_size=(0,0), width=w, height=h*0.083, pos=(0,0)) as topWin:
        dpg.add_image_button(texture_tag="CarRentalLogo", label="Car Rental System", pos=(0,0), width=h*.1, height=h*.075)
        dpg.add_text("Car Rental System", pos=(h*.11,h*.020))
        dpg.bind_item_font(dpg.last_item(), title_font)

        dpg.add_image_button(texture_tag="ProfileLogo", pos=(w*.94,0), width=h*.085, height=h*.075, callback=profile)
        dpg.add_button(label=name, pos=(w/2, h*.03), width=-h*.080)
        dpg.bind_item_theme(dpg.last_item(), "Text_Button_align_right")
        dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_text("Start Date:", pos=(w*0.05, h*0.15), wrap=w-w*0.32*2)
    dpg.bind_item_theme(dpg.last_item(), "text_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_input_text(label="", default_value="mm/dd/yyyy", pos=(w*0.2, h*0.15), width=w*0.2, height=h*0.1)
    dpg.bind_item_theme(dpg.last_item(), "input_box_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_text("End Date:", pos=(w*0.05, h*0.25), wrap=w-w*0.32*2)
    dpg.bind_item_theme(dpg.last_item(), "text_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_input_text(label="", default_value="mm/dd/yyyy", pos=(w*0.2, h*0.25), width=w*0.2, height=h*0.1)
    dpg.bind_item_theme(dpg.last_item(), "input_box_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_text("Number of \nPassengers:", pos=(w*0.05, h*0.35), wrap=w-w*0.32*2)
    dpg.bind_item_theme(dpg.last_item(), "text_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_input_text(label="", default_value="##", pos=(w*0.2, h*0.35), width=w*0.2, height=h*0.1)
    dpg.bind_item_theme(dpg.last_item(), "input_box_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_text("Car Type\n(Make/Model):", pos=(w*0.05, h*0.45), wrap=w-w*0.32*2)
    dpg.bind_item_theme(dpg.last_item(), "text_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_combo(("Choose Model", "Car Model 1", "Car Model 2", "Car Model 3", "Car Model 4"), default_value="Choose Model", callback=make_and_model, pos=(w*0.2, h*0.45), width=w*0.2)
    dpg.bind_item_theme(dpg.last_item(), "dropdown_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_text("Pickup Location:", pos=(w*0.05, h*0.55), wrap=w-w*0.32*2)
    dpg.bind_item_theme(dpg.last_item(), "text_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)
    
    dpg.add_combo(("Choose Location", "Location 1", "Location 2", "Location 3", "Location 4"), default_value="Choose Location", callback=location, pos=(w*0.2, h*0.55), width=w*0.2)
    dpg.bind_item_theme(dpg.last_item(), "dropdown_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_text("Return Location:", pos=(w*0.05, h*0.65), wrap=w-w*0.32*2)
    dpg.bind_item_theme(dpg.last_item(), "text_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)

    dpg.add_combo(("Choose Location", "Location 1", "Location 2", "Location 3", "Location 4"), default_value="Choose Location", callback=location, pos=(w*0.2, h*0.65), width=w*0.2)
    dpg.bind_item_theme(dpg.last_item(), "dropdown_theme")
    dpg.bind_item_font(dpg.last_item(), Res_font)


    dpg.add_button(label="See Availability",pos=(w*0.5, h*0.15), width=w*0.2, height=h*0.1, callback=see_availability)
    dpg.bind_item_theme(dpg.last_item(), "Show_Availability_Button")
    dpg.bind_item_font(dpg.last_item(), title_font)

    if(num_rentals>0):
        with dpg.child_window(border=False, width=w*0.4, height=(h*0.075)*num_rentals, pos=(w*0.5, h*0.3)):
            for rental in range(1, num_rentals+1):
                dpg.add_button(label="Option "+str(rental) + "    >", pos=(0, ((rental-1)*h*.075)), width=w*0.4, height=h*.075, callback=get_availability, user_data="Option "+ str(rental))
                dpg.bind_item_theme(dpg.last_item(), "Availability_Button")
                dpg.bind_item_font(dpg.last_item(), Res_font)

    else:
        dpg.add_text("No Availabilities.\nPlease adjust your search criteria or contact our office.", pos=(w*0.5, h*0.5), wrap=w-w*0.26*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), Res_font)

#bind window font
dpg.bind_item_theme(mainWin, "__win_theme")
dpg.bind_item_theme(topWin, "topWin_theme")

#set up and start gui
dpg.setup_dearpygui()
dpg.set_primary_window(mainWin, True)
dpg.start_dearpygui()
dpg.destroy_context()