import tkinter
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
label = Label(root, text='Tempature Conversion Rates')
label.pack()    #this adds the label on the root gui
root.mainloop() #this shows the gui until I exit out