import dearpygui.dearpygui as dpg
import Current_Upcoming_Reservation_UI
import dbaccess as dbaccess

main_window=""
top_win=""
ID=""
     
'''button functions'''        

def profile(sender, app_data, user_data):
    print("loading user profile")
    
def return_callback(sender, app_data, user_data):
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    
    Current_Upcoming_Reservation_UI.render_reservation_window(ID)

def view_reservation_window(reservation_num, Id):
    global main_window
    global top_win
    global ID
    ID=Id
    
    customer=dbaccess.DBAccess().getCustomer(ID)
    FirstName=customer[0][1]
    LastName=customer[0][2]
    
    reservation=dbaccess.DBAccess().getReservationsByClient(ID)
    reservation=reservation[reservation_num-1]
    vehicle=dbaccess.DBAccess().getVehicle(reservation[2])
    
    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()

    #create window that will contain reservation buttons
    with dpg.window(label="Car Rental System", no_close=True, no_collapse=True, no_resize=True, no_move=True) as mainWin:
        
        #create top bar
        with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, min_size=(0,0), width=w, height=h*.083, pos=(0,0)) as topWin:
            dpg.add_image_button(texture_tag="CarRentalLogo", label="Car Rental System", pos=(0,0), width=h*.1, height=h*.075)
            dpg.add_text("Car Rental System", pos=(h*.11,h*.020))
            dpg.bind_item_font(dpg.last_item(), "title_font")
            
            dpg.add_image_button(texture_tag="ProfileLogo", pos=(w*.94,0), width=h*.085, height=h*.075, callback=profile)
            dpg.add_button(label=str(FirstName) + " " + str(LastName), pos=(w/2, h*.03), width=-h*.080)
            dpg.bind_item_theme(dpg.last_item(), "Text_Button_align_right")
            dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        #reservation information text
        dpg.add_text("Reservation "+str(reservation_num), pos=(w*.1, h*.15))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")
        
        dpg.add_text("Start Date:", pos=(w*0.1, h*0.25), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(reservation[6]), pos=(w*0.25, h*0.25))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("End Date:", pos=(w*0.1, h*0.35), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(reservation[7]), pos=(w*0.25, h*0.35))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Car Make:", pos=(w*0.1, h*0.45), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(vehicle[0][1]), pos=(w*0.25, h*0.45))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("Car Model:", pos=(w*0.5, h*0.45), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(vehicle[0][2]), pos=(w*0.70, h*0.45))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Pickup Location:", pos=(w*0.5, h*0.25), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(reservation[3]), pos=(w*0.70, h*0.25))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("Return Location:", pos=(w*0.5, h*0.35), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(reservation[4]), pos=(w*0.70, h*0.35))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("Invoice Amount:", pos=(w*0.1, h*0.7), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("$"+str(reservation[8]), pos=(w*.25, h*0.7))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_button(label="Return", pos=(w*.35, h*.80), width=w*.3, height=h*.075, callback=return_callback)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")
        
    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")

    dpg.set_primary_window(mainWin, True)

    main_window=mainWin
    top_win=topWin