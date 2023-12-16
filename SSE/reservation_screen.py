import dearpygui.dearpygui as dpg
import Current_Upcoming_Reservation_UI
from Available_Rentals_UI import render_availabilities_window
import dbaccess as dbaccess

main_window=""
top_win=""
ID=""



##Button Functions

def profile(sender, app_data, user_data):
    print("loading user profile")

def make_and_model(sender, app_data, user_data):
    print(user_data)

def location(sender, app_data, user_data):
    print(user_data)

def see_availability(sender, app_data, user_data):
    start_date = dpg.get_value("StartDate")
    end_date = dpg.get_value("EndDate")
    num_passengers = dpg.get_value("NumPassengers")
    model = dpg.get_value("CarModel")
    pickup_location = dpg.get_value("PickupLocation")
    return_location = dpg.get_value("ReturnLocation")
    search_data = [start_date, end_date, num_passengers, model, pickup_location, return_location]
    print("Search Data: ", search_data)


    print("Checking availabilities...")
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    
    render_availabilities_window(ID, [0, [], search_data])

def confirm_reservation():
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    
    Current_Upcoming_Reservation_UI.render_reservation_window()

def render_new_reservation_window(Id):
    global main_window
    global top_win
    global ID
    ID=Id

    customer=dbaccess.DBAccess().getCustomer(ID)
    FirstName=customer[0][1]
    LastName=customer[0][2]
    
    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()
    
    #Main Window
    with dpg.window(label="Car Rental System", no_close=True, no_collapse=True, no_resize=True, no_move=True) as mainWin:
    
        ##Header
        with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, min_size=(0,0), width=w, height=h*0.083, pos=(0,0)) as topWin:
            dpg.add_image_button(texture_tag="CarRentalLogo", label="Car Rental System", pos=(0,0), width=h*.1, height=h*.075)
            dpg.add_text("Car Rental System", pos=(h*.11,h*.020))
            dpg.bind_item_font(dpg.last_item(), "title_font")
    
            dpg.add_image_button(texture_tag="ProfileLogo", pos=(w*.94,0), width=h*.085, height=h*.075, callback=profile)
            dpg.add_button(label=str(FirstName) + " " + str(LastName), pos=(w/2, h*.03), width=-h*.080)
            dpg.bind_item_theme(dpg.last_item(), "Text_Button_align_right")
            dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Start Date:\n(mm/dd/yyyy)", pos=(w*0.05, h*0.15), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_input_text(tag="StartDate", default_value="", pos=(w*0.2, h*0.15), width=w*0.2, height=h*0.1)
        dpg.bind_item_theme(dpg.last_item(), "input_box_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("End Date:\n(mm/dd/yyyy)", pos=(w*0.05, h*0.25), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_input_text(tag="EndDate", default_value="", pos=(w*0.2, h*0.25), width=w*0.2, height=h*0.1)
        dpg.bind_item_theme(dpg.last_item(), "input_box_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Number of \nPassengers:", pos=(w*0.05, h*0.35), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_input_text(tag="NumPassengers", default_value="", pos=(w*0.2, h*0.35), width=w*0.2, height=h*0.1)
        dpg.bind_item_theme(dpg.last_item(), "input_box_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Car Make:", pos=(w*0.05, h*0.45), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_combo(("Choose Model", "SUV", "Compact", "Luxury", "Sedan", "Van", "Truck"), tag="CarModel", default_value="Choose Model", pos=(w*0.2, h*0.45), width=w*0.2)
        dpg.bind_item_theme(dpg.last_item(), "dropdown_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Pickup Location:", pos=(w*0.05, h*0.55), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        dpg.add_combo(("Choose Location", "Athens, GA", "Alpharetta, GA", "Atlanta, GA", "Augusta, GA", "Macon, GA", "Savannah, GA", "Valdosta, GA"), tag="PickupLocation", default_value="Choose Location", callback=location, pos=(w*0.2, h*0.55), width=w*0.2)
        dpg.bind_item_theme(dpg.last_item(), "dropdown_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_text("Return Location:", pos=(w*0.05, h*0.65), wrap=w-w*0.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
        dpg.add_combo(("Choose Location", "Athens, GA", "Alpharetta, GA", "Atlanta, GA", "Augusta, GA", "Macon, GA", "Savannah, GA", "Valdosta, GA"), tag="ReturnLocation", default_value="Choose Location", callback=location, pos=(w*0.2, h*0.65), width=w*0.2)
        dpg.bind_item_theme(dpg.last_item(), "dropdown_theme")
        dpg.bind_item_font(dpg.last_item(), "Res_font")
    
    
        dpg.add_button(label="See Availability",pos=(w*0.5, h*0.15), width=w*0.2, height=h*0.1, callback=see_availability)
        dpg.bind_item_theme(dpg.last_item(), "Show_Availability_Button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")

    dpg.set_primary_window(mainWin, True)
    main_window=mainWin
    top_win=topWin
