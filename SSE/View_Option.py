import dearpygui.dearpygui as dpg
import Current_Upcoming_Reservation_UI
import Available_Rentals_UI
from Visual_Registry import visual_registry
import dbaccess as dbaccess

main_window=""
top_win=""
ID=""
     
'''button functions'''        

def profile(sender, app_data, user_data):
    print("loading user profile")
    

def book(sender, app_data, user_data):
    dpg.show_item("confirmation")
    dpg.configure_item("modal_id2", show=True)

def return_reservations_callback(sender, app_data, user_data):
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)

    Current_Upcoming_Reservation_UI.render_reservation_window(ID)

def return_availabilities_callback(sender, app_data, user_data):
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)

    Available_Rentals_UI.render_availabilities_window(ID)

def view_option_window(option_num, Id):
    global main_window
    global top_win
    global ID
    ID=Id
    
    customer=dbaccess.DBAccess().getCustomer(ID)
    FirstName=customer[0][1]
    LastName=customer[0][2]
    
    vehicle_option=dbaccess.DBAccess().getVehicle(1)   ## Need a DBAccess() call to get vehicles for given search criteria?
    #reservation=dbaccess.DBAccess().getReservationsByClient(ID)
    #reservation=reservation[reservation_num-1]
    #vehicle=dbaccess.DBAccess().getVehicle(reservation[0][2])
    
    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()

    with dpg.window(label="Confirmation", modal=True, show=False, tag="modal_id2", width = w*.4, height = h*.3, no_title_bar=True, pos=(w*.3,300), no_move=True) as confirmationWin:
        dpg.add_text("Reservation Confirmed!", tag="confirmation", pos=(w*.12, h*.1), show=False) 
        dpg.bind_item_theme(dpg.last_item(), "text_theme2")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_button(label="Close", width=w*.13, pos=(w*.14, h*.2), callback=lambda: dpg.configure_item("modal_id2", show=False))
        dpg.bind_item_theme(dpg.last_item(), "new_user_button")
        dpg.bind_item_font(dpg.last_item(), "Res_font")

    #create window that will contain registration buttons
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
        
        #Vehicle information text
        dpg.add_text("Option "+str(option_num), pos=(w*.1, h*.15))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")
            
        dpg.add_text("Car Make:", pos=(w*0.1, h*0.45), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        ##Car Make Text
        # dpg.add_text(str(vehicle_option[0][1]), pos=(w*0.25, h*0.45))
        # dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        # dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text("Car Model:", pos=(w*0.1, h*0.55), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        ##Car Model Text
        # dpg.add_text(str(vehicle_option[0][2]), pos=(w*0.25, h*0.55))
        # dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        # dpg.bind_item_font(dpg.last_item(), "Res_font")

        dpg.add_text("Price:", pos=(w*0.1, h*0.65), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")

        ##Price Text
        # dpg.add_text(str(vehicle_option[0][3]), pos=(w*0.25, h*0.65))
        # dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        # dpg.bind_item_font(dpg.last_item(), "Res_font")
            
        dpg.add_button(label="Book!", pos=(w*.1, h*.75), width=w*.15, height=h*.075, callback=book)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_button(label="Cancel", pos=(w*.4, h*.75), width=w*.15, height=h*.075, callback=return_reservations_callback)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_button(label="Go Back", pos=(w*.7, h*.75), width=w*.15, height=h*.075, callback=return_availabilities_callback)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")

    dpg.set_primary_window(mainWin, True)

    main_window=mainWin
    top_win=topWin