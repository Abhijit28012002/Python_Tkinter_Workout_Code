from tkinter import *

root = Tk()

e = Entry(root,width=50,bg="blue",borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name")


def myClick():
    hello = "Hello "+e.get()
    mylable = Label(root,text=hello)
    mylable.pack()

   
myButton = Button(root,text="Enter Your Name",padx=50,pady=20,command=myClick,fg="blue",bg="black")

myButton.pack()


root.mainloop()