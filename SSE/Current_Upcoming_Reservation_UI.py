import dearpygui.dearpygui as dpg
from reservation_screen import render_new_reservation_window
from View_Registration import view_registration_window
import dbaccess as dbaccess

main_window=""
top_win=""
ID=""

'''button functions'''        
def get_reservation(sender, app_data, user_data):
    print("reservation "+str(user_data))
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    
    view_registration_window(user_data, ID)
    
def new_reservation(sender, app_data, user_data):
    print("Creating new reservation")
    dpg.delete_item(main_window)
    dpg.delete_item(top_win)
    
    render_new_reservation_window()

def profile(sender, app_data, user_data):
    print("loading user profile")

#number of reservations
def getnum_reservation():
    result=dbaccess.DBAccess().getReservationsByClient(ID)
    num_reservation=len(result)
    return num_reservation


def render_reservation_window(Id):
    global main_window
    global top_win
    global ID
    ID=Id

    customer=dbaccess.DBAccess().getCustomer(ID)
    FirstName=customer[0][1]
    LastName=customer[0][2]
    
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
            dpg.add_button(label=str(FirstName) + " " + str(LastName), pos=(w/2, h*.03), width=-h*.080)
            dpg.bind_item_theme(dpg.last_item(), "Text_Button_align_right")
            dpg.bind_item_font(dpg.last_item(), "Res_font")
        
        #create reservation buttons
        dpg.add_text("Current/Upcoming Reservations:", pos=(w*.32, h*.15), wrap=w-w*.32*2)
        dpg.bind_item_theme(dpg.last_item(), "text_theme")
        dpg.bind_item_font(dpg.last_item(), "title_font")
        
        num_reservation = getnum_reservation()
        if(num_reservation>0): 
            with dpg.child_window(border=False, width=w*.7, height=h*.3, pos=(w*.15, h*.3)):
                for res in range(1,num_reservation+1):
                    dpg.add_button(label= "Reservation " + str(res) +"    >", pos=(0, ((res-1)*h*.075)), width=w*.75, height=h*.075, callback=get_reservation, user_data=res)
                    dpg.bind_item_theme(dpg.last_item(), "Reservation_button")
                    dpg.bind_item_font(dpg.last_item(), "Res_font")

        else:
            dpg.add_text("No Reservations", pos=(w*.40, h*.45), wrap=w-w*.26*2)
            dpg.bind_item_theme(dpg.last_item(), "text_theme")
            dpg.bind_item_font(dpg.last_item(), "title_font")
            
        #new reservation buttons               
        dpg.add_button(label="New Reservation", pos=(w*.35, h*.80), width=w*.3, height=h*.075, callback=new_reservation)
        dpg.bind_item_theme(dpg.last_item(), "NewReservation_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")
        
    #bind window font
    dpg.bind_item_theme(mainWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")

    dpg.set_primary_window(mainWin, True)

    main_window=mainWin
    top_win=topWin