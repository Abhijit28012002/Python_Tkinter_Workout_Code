from tkinter import *

# in tkinter first i need to create a window or root widget
root = Tk()

# create a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Hi i am abhijit majumder")
# Showing it onto the screen particular position
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=4,column=0)

root.mainloop()

