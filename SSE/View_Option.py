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
    vehicle_info = user_data[0]
    reservation_info = user_data[1]
    #reservation_info = [start_date, end_date, num_passengers, model, pickup_location, return_location]
    dpg.show_item("confirmation")
    dpg.configure_item("modal_id2", show=True)

    #def addReservation(self, customerID, vehicleID, pickupLocation, dropoffLocation, timeOfPickup, startDate, endDate, invoiceAmount)
    dbaccess.DBAccess().addReservation(ID, vehicle_info[0], vehicle_info[9], vehicle_info[9], "8:00", reservation_info[0], reservation_info[1], vehicle_info[6])
    dbaccess.DBAccess().updateVehicle(vehicle_info[0], vehicle_info[1], vehicle_info[2], vehicle_info[3], vehicle_info[4], vehicle_info[5], vehicle_info[6], vehicle_info[7], False, vehicle_info[9])

def return_reservations_callback(sender, app_data, user_data):
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    dpg.delete_item(confirmation_window)
    
    Current_Upcoming_Reservation_UI.render_reservation_window(ID)

def return_availabilities_callback(sender, app_data, user_data):
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    dpg.delete_item(confirmation_window)
    
    Available_Rentals_UI.render_availabilities_window(ID, user_data)

##vehicle_option = [option number, vehicle, reservation data]
def view_option_window(vehicle_option, Id):
    global main_window
    global top_win
    global confirmation_window
    global ID
    ID=Id

    option_num = vehicle_option[0]
    vehicle = vehicle_option[1]
    reservation_data = vehicle_option[2]
    
    customer=dbaccess.DBAccess().getCustomer(ID)
    FirstName=customer[0][1]
    LastName=customer[0][2]
        
    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()
    
    with dpg.window(label="Confirmation", modal=True, show=False, tag="modal_id2", width = w*.4, height = h*.3, no_title_bar=True, pos=(w*.3,300), no_move=True) as confirmationWin:
        dpg.add_text("Reservation Confirmed!", tag="confirmation", pos=(w*.05, h*.1), show=False) 
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

        dpg.add_text("Car Year:", pos=(w*0.1, h*0.35), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")

        dpg.add_text(str(vehicle[3]), pos=(w*0.25, h*0.35)) ##Year
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")


        dpg.add_text("Car Make:", pos=(w*0.1, h*0.45), wrap=w-w*0.32*2) 
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(vehicle[1]), pos=(w*0.25, h*0.45)) ##Make
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        

        dpg.add_text("Car Model:", pos=(w*0.1, h*0.55), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_text(str(vehicle[2]), pos=(w*0.25, h*0.55)) ##Model
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")


        dpg.add_text("Price:", pos=(w*0.1, h*0.65), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")

        dpg.add_text(str(vehicle[6]), pos=(w*0.25, h*0.65)) ##Price
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "Res_font")

            
        dpg.add_button(label="Book!", pos=(w*.1, h*.75), width=w*.15, height=h*.075, callback=book, user_data=[vehicle, reservation_data])
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_button(label="Reservations", pos=(w*.4, h*.75), width=w*.2, height=h*.075, callback=return_reservations_callback)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_button(label="Options", pos=(w*.7, h*.75), width=w*.15, height=h*.075, callback=return_availabilities_callback, user_data=reservation_data)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")
    dpg.bind_item_theme(confirmationWin, "__win_theme")

    dpg.set_primary_window(mainWin, True)

    main_window=mainWin
    top_win=topWin
    confirmation_window=confirmationWin