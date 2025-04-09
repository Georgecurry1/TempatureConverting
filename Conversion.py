import tkinter
import tkinter.ttk
from tkinter import*
#will try a GUI interface this time
#this is psudo code

def convert1(n):
    #fahrenheit to celsius
    #n is the input
    print("do conversion rate")
    return #converted number return here

def convert2(n):
    #celsius to fahrenheit
    #n is the input
    print("do conversion rate")
    return #converted number return here

#testing python gui, this opens up a blank window titled Conversion
root = tkinter.Tk(screenName=None, baseName=None, className='Conversion', useTk=1)
#see if I can set the size of the defualt window
title = Label(root, text='Tempature Conversion Rates')
title.grid(row=0,column=1)    #this adds the label on the root gui

heading1 = Label(root, text='Conversion 1').grid(row=1, column=0, pady=10)
heading2 = Label(root, text='Conversion 2').grid(row=1, column=2, pady=10)

combo1 = tkinter.ttk.Combobox(root, values=["Fahrenheit","Celsius"])
combo2 = tkinter.ttk.Combobox(root, values=["Fahrenheit","Celsius"])

#set default option in combo box:
combo1.set("Fahrenheit")
combo2.set("Celsius")

combo1.grid(row=2, column=0, pady=10)
combo2.grid(row=2, column=2, pady=10)

#adds text boxes for each option
enterText1 = Entry(root)
enterText1.grid(row=3, column=0, pady=5)

enterText2 = Entry(root)
enterText2.grid(row=3, column=2, pady=5)

#adds submit button
submitButton = Button(root, text= "Submit")
submitButton.grid(row=4, column=1)

root.mainloop() #this shows the gui until I exit out