
from tkinter import *
import time

r = Tk()
r.title("Digital Clock")
r.geometry("630x207")      #size of window
r.resizable(1, 1)

#Add color, font,font size
text_font = ("Boulder", 68, "bold")
background = "lightblue"
foreground = "black"
border_width = 50

label = Label(r, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

#Display the time,miunte,second
def digital_clock():
    time_live = time.strftime("%I:%M:%S:%p")  
     # I stands - hour (1-12) ,  p stands - pm /am ,m stands-minute ,s stands - second
    label.config(text=time_live)
    label.after(100, digital_clock) # update 0.1sec

digital_clock()

r.mainloop()
