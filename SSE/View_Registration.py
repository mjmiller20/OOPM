import dearpygui.dearpygui as dpg
import Current_Upcoming_Reservation_UI
main_window=""
top_win=""

     
'''button functions'''        

def profile(sender, app_data, user_data):
    print("loading user profile")
    
def return_callback(sender, app_data, user_data):
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    
    Current_Upcoming_Reservation_UI.render_reservation_window()

def view_registration_window(registration_num):
    name="John Doe"
    
    global main_window
    global top_win

    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()

    #create window that will contain registration buttons
    with dpg.window(label="Car Rental System", no_close=True, no_collapse=True, no_resize=True, no_move=True) as mainWin:
        
        #create top bar
        with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, min_size=(0,0), width=w, height=h*.083, pos=(0,0)) as topWin:
            dpg.add_image_button(texture_tag="CarRentalLogo", label="Car Rental System", pos=(0,0), width=h*.1, height=h*.075)
            dpg.add_text("Car Rental System", pos=(h*.11,h*.020))
            dpg.bind_item_font(dpg.last_item(), "title_font")
            
            dpg.add_image_button(texture_tag="ProfileLogo", pos=(w*.94,0), width=h*.085, height=h*.075, callback=profile)
            dpg.add_button(label=name, pos=(w/2, h*.03), width=-h*.080)
            dpg.bind_item_theme(dpg.last_item(), "Text_Button_align_right")
            dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        #reservation information text
        dpg.add_text("Reservation "+str(registration_num), pos=(w*.1, h*.15))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")
        
        dpg.add_text("Start Date:", pos=(w*0.1, h*0.25), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("getStartDate", pos=(w*0.25, h*0.25))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("End Date:", pos=(w*0.1, h*0.35), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("getEndDate", pos=(w*0.25, h*0.35))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Number of \nPassengers:", pos=(w*0.1, h*0.45), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("getNumPassengers", pos=(w*0.25, h*0.45))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Car Make:", pos=(w*0.1, h*0.55), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("getMake", pos=(w*0.25, h*0.55))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("Car Model:", pos=(w*0.1, h*0.65), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("getCarModel", pos=(w*0.25, h*0.65))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Pickup Location:", pos=(w*0.1, h*0.75), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("getPickupLocation", pos=(w*0.25, h*0.75))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("Return Location:", pos=(w*0.1, h*0.85), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("getReturnLocation", pos=(w*0.25, h*0.85))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_button(label="Return", pos=(w*.5, h*.75), width=w*.3, height=h*.075, callback=return_callback)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")
        
    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")

    dpg.set_primary_window(mainWin, True)

    main_window=mainWin
    top_win=topWin