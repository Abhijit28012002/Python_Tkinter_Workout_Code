from tkinter import *

root = Tk()

def myClick():
    mylable = Label(root,text="Look! I Clicked Button!")
    mylable.pack()

   
myButton = Button(root,text="Click Me",padx=50,pady=20,command=myClick,fg="blue",bg="black")

myButton.pack()


root.mainloop()