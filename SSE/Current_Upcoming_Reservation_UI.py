import dearpygui.dearpygui as dpg
       
'''button functions'''        
def get_reservation(sender, app_data, user_data):
    print(user_data)
    
def new_reservation(sender, app_data, user_data):
    print("Creating new reservation")

def profile(sender, app_data, user_data):
    print("loading user profile")

def render_reservation_window():
    num_reservation=5
    name="John Doe"

    '''Themes'''
    #set theme for current/upcoming reservation buttons
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

    with dpg.theme(tag="Text_Button_align_right"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 1, .5)
            
    #set theme for text
    with dpg.theme(tag="text_theme"):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0,0,255))

    #set theme for window
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
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255,255,255))

    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()


    '''font'''
    with dpg.font_registry():
        #default_font=dpg.add_font("Quicksand-VariableFont_wght.ttf", h*.028)
        Res_font=dpg.add_font("Arial.otf", h*.030)
        title_font=dpg.add_font("Arial.otf", h*.05)
        #third_font


    #create window that will contain registration buttons
    with dpg.window(label="Car Rental System", no_close=True, no_collapse=True, no_resize=True, no_move=True) as mainWin:
        
        #create top bar
        with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, min_size=(0,0), width=w, height=h*.083, pos=(0,0)) as topWin:
            dpg.add_image_button(texture_tag="CarRentalLogo", label="Car Rental System", pos=(0,0), width=h*.1, height=h*.075)
            dpg.add_text("Car Rental System", pos=(h*.11,h*.020))
            dpg.bind_item_font(dpg.last_item(), title_font)
            
            dpg.add_image_button(texture_tag="ProfileLogo", pos=(w*.94,0), width=h*.085, height=h*.075, callback=profile)
            dpg.add_button(label=name, pos=(w/2, h*.03), width=-h*.080)
            dpg.bind_item_theme(dpg.last_item(), "Text_Button_align_right")
            dpg.bind_item_font(dpg.last_item(), Res_font)
        
        #create reservation buttons
        dpg.add_text("Current/Upcoming Reservations:", pos=(w*.32, h*.15), wrap=w-w*.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), title_font)
        
        if(num_reservation>0): 
            with dpg.child_window(border=False, width=w*.7, height=h*.3, pos=(w*.15, h*.3)):
                for res in range(1,num_reservation+1):
                    dpg.add_button(label= "Reservation " + str(res) +"    >", pos=(0, ((res-1)*h*.075)), width=w*.75, height=h*.075, callback=get_reservation, user_data="reservation "+str(res))
                    dpg.bind_item_theme(dpg.last_item(), "Reservation_button")
                    dpg.bind_item_font(dpg.last_item(), Res_font)

        else:
            dpg.add_text("No Reservations", pos=(w*.40, h*.45), wrap=w-w*.26*2)
            dpg.bind_item_theme(dpg.last_item(), "text_theme")
            dpg.bind_item_font(dpg.last_item(), title_font)
            
        #new reservation buttons               
        dpg.add_button(label="New Reservation", pos=(w*.35, h*.80), width=w*.3, height=h*.075, callback=new_reservation)
        dpg.bind_item_theme(dpg.last_item(), "NewReservation_button")
        dpg.bind_item_font(dpg.last_item(), title_font)
        
    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")

    dpg.set_primary_window(mainWin, True)
