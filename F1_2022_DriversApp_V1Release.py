#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import necessary modules
from tkinter import *
from tkinter import ttk
import requests
import json

root = Tk()
root.geometry("800x300")
root.title("F1 Desktop Application")
root.iconbitmap("formula1_logo.ico")
root.resizable(False, False)

#initialized variables
error_message = " does not Exist. Search Again!"

#generate 2022 drivers-list through api
drivers_list_request = requests.get("http://ergast.com/api/f1/2022/drivers.json")

#initialize empty-list
drivers_list = []

drivers_list_object = json.loads(drivers_list_request.content)

for elements in drivers_list_object["MRData"]["DriverTable"]["Drivers"]:
    drivers_list.append(elements["givenName"] + " " + elements["familyName"])


#functions

#grab user-input from entry-box
def grab_user_input():
    
    return entry_box.get()
    
    
# Search functionality for entry-box and listbox
def check(e):
    
    v= grab_user_input()

    if v=='':
        hide_button(menu)
    
    else:
        
        data=[]
        for item in drivers_list:
            if v.lower() in item.lower():
                data.append(item)
                
        #on instance where there are 0 elements in data (there are 0 matches to elements in drivers_list)
        if len(data) == 0:
            
            data.append(v)
                        
        update(data)
        show_button(menu)

def update(data):
    
   # Clear the Combobox
   menu.delete(0, END)
   # Add values to the combobox
   for value in data:
        menu.insert(END,value)
        
def fillout(event):
    
    try:
        
        entry_box.delete(0,END)
        
        entry_box.insert(0,menu.get(menu.curselection()))
        
        hide_button(menu)
        
    #handle a complete deletion of entry-box via cursor double tap
    except:
        
        pass

#functions responsible for hiding widgets and showing widgets(back in their original place)
def hide_button(widget):
    
    widget.grid_remove()
    
def show_button(widget):
    
    widget.grid()
    
    
#api functions, to fetch data
def full_name(driver):
            
    response = requests.get("http://ergast.com/api/f1/drivers/{}.json".format(driver))
        
    response_object = json.loads(response.content)
        
    name = response_object["MRData"]["DriverTable"]["Drivers"][0]["givenName"] + " " + response_object["MRData"]["DriverTable"]["Drivers"][0]["familyName"]

    driver_name_label.configure(text = name)
    
    
def team(driver):
        
    response = requests.get("http://ergast.com/api/f1/current/drivers/{}/constructors.json".format(driver))

    response_object = json.loads(response.content)

    team = response_object["MRData"]["ConstructorTable"]["Constructors"][0]["name"]
    
    team_api.configure(text = team)
        
def nationality(driver): 
    
    response = requests.get("http://ergast.com/api/f1/drivers/{}.json".format(driver))

    response_object = json.loads(response.content)

    nationality = response_object["MRData"]["DriverTable"]["Drivers"][0]["nationality"]

    nationality_api.configure(text = nationality)
    
    
def driver_code(driver): 
    
    response = requests.get("http://ergast.com/api/f1/drivers/{}.json".format(driver))
        
    response_object = json.loads(response.content)
        
    code = response_object["MRData"]["DriverTable"]["Drivers"][0]["code"]
    
    code_api.configure(text = code)

        
def wins(driver): 

    response = requests.get("http://ergast.com/api/f1/drivers/{}/results/1.json".format(driver))

    response_object = json.loads(response.content)
        
    wins = response_object["MRData"]["total"]

    wins_api.configure(text = wins)
        
def podiums(driver):

    #podiums is sum of 1st, 2nd, 3rd place finishes

    #1st place finishes

    response = requests.get("http://ergast.com/api/f1/drivers/{}/results/1.json".format(driver))

    response_object = json.loads(response.content)

    wins = int(response_object["MRData"]["total"])

    #2nd place finishes

    response_ii = requests.get("http://ergast.com/api/f1/drivers/{}/results/2.json".format(driver))

    response_ii_object = json.loads(response_ii.content)

    response_ii_amount = int(response_ii_object["MRData"]["total"])

    #3rd place finishes 

    response_iii = requests.get("http://ergast.com/api/f1/drivers/{}/results/3.json".format(driver))

    response_iii_object = json.loads(response_iii.content)

    response_iii_amount = int(response_iii_object["MRData"]["total"])

    podiums = str(wins + response_ii_amount + response_iii_amount)

    podiums_api.configure(text = podiums)
        

def poles(driver): 

    response = requests.get("http://ergast.com/api/f1/drivers/{}/qualifying/1.json".format(driver))

    response_object = json.loads(response.content)

    poles = response_object["MRData"]["total"]

    poles_api.configure(text = poles)        
    
    
def championships(driver):
    
    response = requests.get("http://ergast.com/api/f1/drivers/{}/driverStandings/1/seasons.json".format(driver))

    response_object = json.loads(response.content)

    championships = response_object["MRData"]["total"]

    championships_api.configure(text = championships)
        
    
def standing(driver):
        
    response = requests.get("http://ergast.com/api/f1/current/drivers/{}/driverStandings.json".format(driver))

    response_object = json.loads(response.content)

    position = response_object["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["position"]

    points = response_object["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["points"]

    standing = "{} ({} pts)".format(position, points)

    standing_api.configure(text = standing)

    
#convert user-input into an id to pass to api functions
def convert_user_input(): 
        
    edge_case_inputs = ["Max Verstappen", "Kevin Magnussen", "Mick Schumacher"]
    
    special_case = "Nyck de Vries"
        
    user_input = grab_user_input()
    
    if user_input in edge_case_inputs:
        
        lower_user_input = user_input.lower().replace(" ", "_")
        
        return lower_user_input
    
    #very unique case
    
    elif user_input == special_case:
        
        lower_user_input = "de_vries"
        
        return lower_user_input
    
    elif user_input in drivers_list:
            
            #i.e, Daniel Ricciardo -> ricciardo
            lower_user_input = user_input.lower().split(" ")[1]
    
            return lower_user_input
    
    #handle case of invalid input 
    else:
        
        return error_message
    
def error_message_display(message):
    
    #hide menu button
    hide_button(menu)
    
    error_label = Label(left_frame, text = message)
    error_label.grid(row = 3, column = 0)
    
    #destroy it after a few seconds
    left_frame.after(5000, error_label.destroy)

    

#search is looking for event, either: <enter button> on keyboard or directly pressing search button
#checks user-input before running api functions
def search(e):
    
    
    converted_user_input = convert_user_input()
    
    if converted_user_input == error_message:
    
        error_message_display((grab_user_input() + error_message))
        
        
    else:
        
        
        #fast-run time
        full_name(convert_user_input())

        #fast-run time
        team(convert_user_input())
        
        #fast-run time
        nationality(convert_user_input())

        #fast-run time
        driver_code(convert_user_input())

        #fast-run time
        wins(convert_user_input())
        
        #fast-run time
        podiums(convert_user_input())

        #fast-run time
        poles(convert_user_input())

        #fast-run time
        championships(convert_user_input())

        #fast-run time
        standing(convert_user_input())

        #show the frame with the generated content
        show_button(main_frame)
        

#initalized widgets
#left_frame

left_frame = LabelFrame(root, width = 275, height = 300)
left_frame.grid(row = 1, column = 0, sticky = SE)
left_frame.grid_propagate(False)

search_label = Label(left_frame, text = "Search Driver", font = ("Arial bold", 12))
search_label.grid(row = 0, column = 0, pady = 10)

entry_box = Entry(left_frame, bd = 5)
entry_box.grid(row = 1, column = 0, padx = 35, pady = 40)
#bind every keyboard input to function, check
entry_box.bind('<KeyRelease>',check)

#dual binding of pressing search_button directly or just pressing enter
#pass something into the lambda
search_button = Button(left_frame, text = "search", command = lambda: search(1))
search_button.grid(row = 1, column = 1, padx = 5)
root.bind("<Return>", search)

menu= Listbox(left_frame, height = 7)
menu.grid(row = 2, column = 0)
#bind any user click in listbox to function, fillout
menu.bind("<<ListboxSelect>>",fillout)

#main_frame

main_frame = LabelFrame(root, width = 575, height = 300)
main_frame.grid(row = 1, column = 1, sticky = SE)
main_frame.grid_propagate(False)

driver_name_label = Label(main_frame, text = "", font = ("Arial", 15))
driver_name_label.grid(row = 0, column = 0,pady = 30)

team_label = Label(main_frame, text = "TEAM", font = ("Arial", 10))
team_label.grid(row = 1, column = 0, sticky = W)

team_api = Label(main_frame, text = "", font = ("Arial", 10))
team_api.grid(row = 1, column = 1, sticky = W)

nationality_label = Label(main_frame, text = "NATIONALITY", font = ("Arial", 10))
nationality_label.grid(row = 2, column = 0, sticky = W)

nationality_api = Label(main_frame, text = "", font = ("Arial", 10))
nationality_api.grid(row = 2, column = 1, sticky = W)

driver_code_label = Label(main_frame, text = "DRIVER CODE", font = ("Arial", 10))
driver_code_label.grid(row = 3, column = 0, sticky = W)

code_api = Label(main_frame, text = "", font = ("Arial", 10))
code_api.grid(row = 3, column = 1, sticky = W)

wins_label = Label(main_frame, text = "WINS", font = ("Arial", 10))
wins_label.grid(row = 4, column = 0, sticky = W)

wins_api = Label(main_frame, text = "", font = ("Arial", 10))
wins_api.grid(row = 4, column = 1, sticky = W)

podiums_label = Label(main_frame, text = "PODIUMS", font = ("Arial", 10))
podiums_label.grid(row = 1, column = 2, sticky = W, padx = 15)

podiums_api = Label(main_frame, text = "", font = ("Arial", 10))
podiums_api.grid(row = 1, column = 3, sticky = W,  padx = 15)

poles_label = Label(main_frame, text = "POLES", font = ("Arial", 10))
poles_label.grid(row = 2, column = 2, sticky = W, padx = 15)

poles_api = Label(main_frame, text = "", font = ("Arial", 10))
poles_api.grid(row = 2, column = 3, sticky = W, padx = 15)

world_championships_label = Label(main_frame, text = "WORLD CHAMPIONSHIPS", font = ("Arial", 10))
world_championships_label.grid(row = 3, column = 2, padx = 15, sticky = W)

championships_api = Label(main_frame, text = "", font = ("Arial", 10))
championships_api.grid(row = 3, column = 3, padx = 15, sticky = W)

current_standing_label = Label(main_frame, text = "F1 2022 STANDING", font = ("Arial", 10))
current_standing_label.grid(row = 4, column = 2, padx = 15, sticky = W)

standing_api = Label(main_frame, text = "", font = ("Arial", 10))
standing_api.grid(row = 4, column = 3, padx = 15, sticky = W)   



#initalized conditions

hide_button(menu)
hide_button(main_frame)

root.mainloop()


# In[ ]:




