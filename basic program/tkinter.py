# import tkinter module
from tkinter import *

# creating main tkinter window/toplevel
master = Tk()
master.title("Student Details")
#master.geometry("400x600")
# this wil create a label widget

Label(master, text = "Name:").grid(row = 0, column = 0, sticky = W, pady = 2)
Label(master, text = "USN:").grid(row = 1, column = 0, sticky = W, pady = 2)
Label(master, text = "SEM:").grid(row = 2, column = 0, sticky = W, pady = 2)
Label(master, text = "Sport:").grid(row = 3, column = 0, sticky = W, pady = 2)
e1 = Entry(master).grid(row = 0, column = 1, pady = 2)
e2 = Entry(master).grid(row = 1, column = 1, pady = 2)
e3 = Entry(master).grid(row = 2, column = 1, pady = 2)
Label(master, text = "CGPA:").grid(row = 7, column = 0, sticky = W, pady = 2)
Label(master, text = "Elective:").grid(row = 8, column = 0, sticky = W, pady = 2)
e4 = Entry(master).grid(row = 7, column = 1, pady = 2)
e5 = Entry(master).grid(row = 8, column = 1, pady = 2)
Checkbutton(master,text="Cricket").grid(row=4, column=1,sticky=W,columnspan=2)
Checkbutton(master,text="Volleyball").grid(row=5, column=1,sticky=W,columnspan=2)
Checkbutton(master,text="badminton").grid(row=6, column=1,sticky=W,columnspan=2)
Button(master,text="save").grid(row=9,column=0,sticky=E)
Button(master,text="submit").grid(row=9,column=4,sticky=E)
mainloop()