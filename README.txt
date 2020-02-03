Module timer designed to track the hours spent on each module and personal project in my second semester of 
my computer science conversion postgrad at UCD. 
The timer is implemented as a GUI built using Tkinter.

V1 was purely a terminal based program, whereby the user was prompted manually for the number of minutes they intended to study, followed by a prompt for the module code in particular. 
Using the Gspread API, which enables interaction between Python scripts and Google Sheets, It was possible to locate and update a cell based on todays date and the module code in question, i.e. the intersection of these x and y coordinates would represent a module being worked on, on a particular date. 
I then made sure to grab a cells value and store it prior to update, so that this could be added to the newly elapsed time, thereby keeping daily track of hours spent on a particular module. 

V2 was developed to have a more accessible GUI version of the program using Tkinter. 
The user is again prompted for the mount of time they intend to spend and the module they were working on (dropdown menu).

Problems and suggested future edits:
The timer appears in a new window - how to solve this?
The submit and dropdown selection fields having poor visibility. 
Potentially building a database of quotes via web-scraping which would appear at random at the end of a run. 

