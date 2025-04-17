from tkinter import*
import tkinter
import tkinter.messagebox
import tkinter.ttk
#functions

def toFahrenheit(n):
    #fahrenheit to celsius
    #n is the input
    result = (n-32)* 5/9
    return result

def toCelsius(n):
    #celsius to fahrenheit
    result = (n * 9/5) + 32
    return result

def onSubmit(self):
    #checks to see if both options are different, if so, it does the conversion based on  combobox 1
    if combo2.get() != combo1.get():
        #if both boxes are different then proceed
        if combo1.get()=="Fahrenheit":
            num = toFahrenheit(int(enterText1.get()))#convert the number we get from the field to F
            answer = 'The conversion between Fahrenheit and Celsius = '+str(round(num,1))
            tkinter.messagebox.showinfo(title="Answer", message=answer)
            root.destroy()
        else:
            num = toCelsius(int(enterText1.get()))
            answer = 'The conversion between Celsius and Fahrenheit = '+str(round(num,1))
            tkinter.messagebox.showinfo(title="Answer", message=answer) #display a popup GUI with answer!
            root.destroy()

root = tkinter.Tk(screenName=None, baseName=None, className='Conversion', useTk=1)
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
enterText1.grid(row=3, column=1, pady=5)


#adds submit button
submitButton = Button(root, text= "Submit")
submitButton.grid(row=4, column=1, pady=15)

#once the submit button is pressed, check to see if both dropdown options are different.
#if they are then do the conversion. Then output it on the screen

submitButton.bind("<Button-1>", onSubmit) #run the onSubmit function when left button is clicked on button

root.mainloop() #this shows the gui until user exits out