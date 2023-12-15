import dearpygui.dearpygui as dpg
from Current_Upcoming_Reservation_UI import render_reservation_window
import dbaccess as dbaccess


import hashlib
import uuid

login_window = ""
top_window = ""
invalid_login_win = ""
new_account_win = ""

def resetErrors():
        dpg.hide_item("invalid_login1")
        dpg.hide_item("invalid_login2")

def login_callback(sender, app_data, user_data):

    email = dpg.get_value("Username_text")
    password = dpg.get_value("Password_text")

    if email == "" or password == "":
        resetErrors()
        dpg.show_item("invalid_login2")
        dpg.configure_item("modal_id2", show=True)

    else:
        #hash and salt password
        salt = uuid.uuid4().hex
        password_hash = hashlib.sha256(str(password).encode('utf-8')).hexdigest()

        #db call to get info
        result = dbaccess.DBAccess().getCustomerByEmailAndHash(email, str(password_hash))
        
        if(len(result) >= 1):
            dpg.delete_item(login_window)
            dpg.delete_item(top_window)
            dpg.delete_item(invalid_login_win)
            dpg.delete_item(new_account_win)

            render_reservation_window(result[0][0])

        else:
            resetErrors()
            dpg.show_item("invalid_login1")
            dpg.configure_item("modal_id2", show=True)

def create_account():

    name = dpg.get_value("full_name_text")
    email = dpg.get_value("new_Username_text")
    password = dpg.get_value("new_Password_text")
    phone = "111"

    if name == "" or email == "" or password == "":
        dpg.show_item("invalid_creation")

    else:
        firstname = ""
        lastname = ""

        #split name string by spaces
        names = name.split()
        firstname = names[0]

        #if more than 2 names store in last name value
        if(len(names) > 1):
            i = 1
            while i < len(names):
                lastname += names[i] + " "
                i = i+1

        #hash password
        salt = uuid.uuid4().hex
        password_hash = hashlib.sha256(str(password).encode('utf-8')).hexdigest()

        if dbaccess.DBAccess().addCustomer(firstname, lastname, email, str(phone), str(password_hash)):
            dpg.hide_item("invalid_creation")

            dpg.configure_item("modal_id", show=False)
        else:
            dpg.show_item("invalid_creation")

def render_login_window():
    global login_window
    global top_window
    global new_account_win
    global invalid_login_win

    w=dpg.get_viewport_width()
    h=dpg.get_viewport_height()

    with dpg.window(label="Invalid login", modal=True, show=False, tag="modal_id2", width = w*.4, height = h*.3, no_title_bar=True, pos=(w*.3,300), no_move=True) as invalidLoginWin:
        dpg.add_text(" Invalid Login!", tag="invalid_login1", pos=(w*.12, h*.1), show=False) 
        dpg.bind_item_theme(dpg.last_item(), "text_theme2")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_text("Invalid Params!", tag="invalid_login2", pos=(w*.12, h*.1), show=False) 
        dpg.bind_item_theme(dpg.last_item(), "text_theme2")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_button(label="Close", width=w*.13, pos=(w*.14, h*.2), callback=lambda: dpg.configure_item("modal_id2", show=False))
        dpg.bind_item_theme(dpg.last_item(), "new_user_button")
        dpg.bind_item_font(dpg.last_item(), "Res_font")

    with dpg.window(label="New Account", modal=True, show=False, tag="modal_id", width = w*.9, height = h*.8, no_title_bar=True, pos=(w*.05,100), no_move=True) as newAccountWin:

        dpg.add_text("Create a New Account ", pos=(w*.34, h*.20))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_text("Full Name: ", pos=(w*.05, h*.35))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_input_text(tag="full_name_text", pos=(w*.2, h*.35), width=w*.65, height=h*.075)
        dpg.bind_item_theme(dpg.last_item(), "input_text_theme")
        dpg.bind_item_font(dpg.last_item(), "title_font")
    
        dpg.add_text("Email: ", pos=(w*.10, h*.45))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_input_text(tag="new_Username_text", pos=(w*.2, h*.45), width=w*.65, height=h*.075)
        dpg.bind_item_theme(dpg.last_item(), "input_text_theme")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_text(" Password: ", pos=(w*.05, h*.55)) 
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_input_text(tag="new_Password_text", pos=(w*.2, h*.55), width=w*.65, height=h*.15, password=True)
        dpg.bind_item_theme(dpg.last_item(), "input_text_theme")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_text("Failed to create account!", tag= "invalid_creation", pos=(w*.33, h*.60), show=False)
        dpg.bind_item_theme(dpg.last_item(), "text_theme2")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        with dpg.group(horizontal=True):
            dpg.add_button(label="Create Account", width=w*.13, pos=(w*.32, h*.70), callback=lambda: create_account())
            dpg.bind_item_theme(dpg.last_item(), "new_user_button")
            dpg.bind_item_font(dpg.last_item(), "Res_font")
            dpg.add_button(label="Cancel", width=w*.13, pos=(w*.48, h*.70), callback=lambda: dpg.configure_item("modal_id", show=False))
            dpg.bind_item_theme(dpg.last_item(), "new_user_button")
            dpg.bind_item_font(dpg.last_item(), "Res_font")

    #create top bar
    with dpg.window(label="Car Rental System", no_close=True, no_collapse=True, no_resize=True, no_move=True) as loginWin:
        with dpg.window(no_title_bar=True, no_close=True, no_collapse=True, no_resize=True, no_move=True, min_size=(0,0), width=w, height=h*.083, pos=(0,0)) as topWin:
            dpg.add_image_button(texture_tag="CarRentalLogo", label="Car Rental System", pos=(0,0), width=h*.1, height=h*.075)
            dpg.add_text("Car Rental System", pos=(h*.11,h*.020))
            dpg.bind_item_font(dpg.last_item(), "title_font")
            
        dpg.add_text("Welcome!", pos=(w*.44, h*.25))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_text("Please Log in using your Email and Password", pos=(w*.25, h*.30))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")


        dpg.add_text("Email: ", pos=(w*.10, h*.45))
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_input_text(tag="Username_text", pos=(w*.2, h*.45), width=w*.65, height=h*.075)
        dpg.bind_item_theme(dpg.last_item(), "input_text_theme")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_text(" Password: ", pos=(w*.05, h*.55)) 
        dpg.bind_item_theme(dpg.last_item(), "text_theme1")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        dpg.add_input_text(tag="Password_text", pos=(w*.2, h*.55), width=w*.65, height=h*.15, password=True)
        dpg.bind_item_theme(dpg.last_item(), "input_text_theme")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        #Login button             
        dpg.add_button(label="Login", pos=(w*.35, h*.70), width=w*.3, height=h*.075, callback=login_callback)
        dpg.bind_item_theme(dpg.last_item(), "Login_button")
        dpg.bind_item_font(dpg.last_item(), "title_font")

        #new user text             
        dpg.add_button(tag="new_user", label="New User? Create an Account",  pos=(w*.35, h*.80), width=w*.3, height=h*.075, callback=lambda: dpg.configure_item("modal_id", show=True))
        dpg.bind_item_theme(dpg.last_item(), "new_user_button")
        dpg.bind_item_font(dpg.last_item(), "Res_font")

    dpg.bind_item_theme(loginWin, "__win_theme")
    dpg.bind_item_theme(topWin, "topWin_theme")
    dpg.bind_item_theme(newAccountWin, "__win_theme")
    dpg.bind_item_theme(invalidLoginWin, "__win_theme")

    dpg.set_primary_window(loginWin, True)

    login_window = loginWin
    top_window = topWin
    new_account_win = newAccountWin
    invalid_login_win = invalidLoginWin

