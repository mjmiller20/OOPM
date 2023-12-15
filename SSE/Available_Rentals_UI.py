import dearpygui.dearpygui as dpg
import Current_Upcoming_Reservation_UI
from View_Option import view_option_window
import reservation_screen
##from reservation_screen import render_new_reservation_window
import dbaccess as dbaccess

def get_option(sender, app_data, user_data):
    ##user_data = [option number, vehicle, reservation data]
    print("option "+str(user_data))
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)

    view_option_window(user_data, ID)   ##user_data is the vehicle associated with the option the user is selecting

##search_criteria = [start_date, end_date, num_passengers, model, pickup_location, return_location]
def get_options(search_criteria):
    ##Note: this only gets vehicles that are currently available.  Future work required to get vehicles that are available for future dates.
    total_vehicles=dbaccess.DBAccess().getVehicles()
    available_vehicles = []
    for vehicle in total_vehicles:
        if vehicle[8] == True and vehicle[9] == search_criteria[4] and vehicle[7] == search_criteria[3]:
            available_vehicles.append(vehicle)
    return available_vehicles

def profile(sender, app_data, user_data):
    print("loading user profile")

def return_callback(sender, app_data, user_data):
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    
    reservation_screen.render_new_reservation_window()


def render_availabilities_window(Id, search_data):
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
    
        options = get_options(search_data)
        if(len(options)>0): 
            with dpg.child_window(border=False, width=w*.7, height=h*.3, pos=(w*.15, h*.3)):
                for res in range(1,len(options)+1):
                    dpg.add_button(label= "Option " + str(res) +"    >", pos=(0, ((res-1)*h*.075)), width=w*.75, height=h*.075, callback=get_option, user_data=[res, options[res-1], search_data])
                    dpg.bind_item_theme(dpg.last_item(), "Reservation_button")
                    dpg.bind_item_font(dpg.last_item(), "Res_font")

        else:
            dpg.add_text("No Availabilities.  Please adjust your search criteria and try again.", pos=(w*.40, h*.45), wrap=w-w*.26*2)
            dpg.add_button(label="Go Back", pos=(0, ((res-1)*h*.075)), width=w*.75, height=h*.075, callback=return_callback)
            dpg.bind_item_theme(dpg.last_item(), "text_theme")
            dpg.bind_item_font(dpg.last_item(), "title_font")

    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")

    dpg.set_primary_window(mainWin, True)
    main_window=mainWin
    top_win=topWin
