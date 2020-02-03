
from tkinter import *
import time 
import tkinter as tk
import webbrowser


# define click - this function will be called when the submit button in the GUI is pressed
def click():
	''' This function collects the intended time spent studying and the module in question after the submit button is pressed in the GUI'''
	
	# open the spreadsheet automatically 
	webbrowser.open('https://docs.google.com/spreadsheets/d/12drdLLucIdTk4hDWE1c_lFNpb8TWZOA2jMv9X9VpmGk/edit?usp=sharing') # this is the spreadsheet
	
	entered_text = textentry.get() # will collect the amount of minutes  
	entered_text = int(entered_text)
	
	global_mod = module_choice.get() # will collect the module in question  

	moduleTimer(entered_text,global_mod) # this then calls the moduleTimer class which commences the timer countdown 

# tutorial info obtained from : https://youtu.be/cnPlKLEGR7E
def updateSheet(module,time): 
	''' This function updates the Google Sheet with time spent studying after the countdown timer has elapsed'''
	
	import gspread # gspread Python API that interfaces with google Sheets 
	from oauth2client.service_account import ServiceAccountCredentials

	from datetime import date # find todays date  
	from time import strftime 
	today = date.today()
	today = today.strftime('%d/%m/%Y') # necessary step to format dates in a format consistent with the spreadsheet design

	scope = ['https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
	client = gspread.authorize(creds)
	sheet = client.open("semester2").sheet1

	
	mod_choice = sheet.find(module) # find the correct column corresponding to the module being worked on 
	
	date = sheet.find(today) 

	cell = (mod_choice.col,date.row) # the cell in question is found by the intersection of the module choice and todays date

	current_value = sheet.cell(date.row,mod_choice.col).value # if the cell already has a time entry - then the program retains it, so as not to overwrite it 

	time_decimal_hour = (time/60)/60 # time formatting 
	

	if current_value == '':
		current_value = 0
	else:
		current_value = float(current_value)
	new_total = current_value + time_decimal_hour # the new value is the sum of the previous entry plus the elapsed time in this run 

	sheet.update_cell(date.row,mod_choice.col,new_total) # update the value 

# timer was created by adpating code from this Stack entry answer from Bryan Oakley: https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter 
class moduleTimer(tk.Tk):
	''' Timer class that counts down based upon the time entered in the Tkinter textentry box'''
    def __init__(self,remaining,module):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=100, height=20)
        self.label.pack()
        self.remaining = remaining
        self.remaining = self.remaining * 60
        self.time = self.remaining 
        self.countdown(self.remaining) # automatically calls the countdown method 
        self.module = module # necessary to transfer to updateSheet function [scoping issue] 

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining


        if self.remaining <= 0:
            self.label.configure(text="Time's up, take a few minutes if you need it.") 


            print("self.module: ",self.module)
            updateSheet(self.module,self.time) # calls the updateSheet function delivering the module name and the time elapsed

        else:
            self.mins, self.secs = divmod(self.remaining,60)
            self.timeformat = '{:02d}:{:02d}'.format(self.mins, self.secs) # format seconds and minutes 
            self.label.configure(text=self.timeformat)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

# options for dropdown menu in GUI dropdwon menu 
OPTIONS = [
"COMP47350",
"COMP30830",
"COMP30820",
"COMP30660",
"COMP30650",
"COMP20230",
"PERSONAL"
]

## GUI design- tutorial info obtained from: https://youtu.be/_lSNIrR1nZU

# create a window 
### main
window = Tk()
window.title("Comp Sci Timer") # name the window 
window.configure(background="black")

### image for program 
dog = PhotoImage(file="dog.gif") # local file
Label(window, image = dog, bg="grey").grid(row=0, column=0, sticky=W)

#### HOW LONG

# create label
Label(window,text="How many minutes would you like to study for?",bg = "black", fg ="white").grid(row=1, column=0,sticky = W)
# create a text entry box for the minutes
textentry = Entry(window, width=10, bg ="white")
textentry.grid(row=1,column=1,sticky=W) 

### WHAT MODULE 

#dropdown menu 
Label(window,text="What are you working on?",bg = "black", fg ="white").grid(row=3, column=0,sticky = W)

module_choice = StringVar(window)
module_choice.set(OPTIONS[0])
dropdown = OptionMenu(window,module_choice, *OPTIONS)
dropdown.grid(row=3,column=1,sticky=W)

### submit button 
Button(window, text="SUBMIT", width=6, command=click,bg="red",fg="red").grid(row=5,column=0,sticky=W) # click function is invoked here when submit button is pressed

### main loop run
window.mainloop()

