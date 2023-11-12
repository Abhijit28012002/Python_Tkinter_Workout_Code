from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Create code')

r =IntVar()
r.set("2")

MODES =[
    ("Pepperoni","Pepperoni"),
    ("cheese","cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]
pizz = StringVar()
pizz.set("Pepperoni")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizz,value=mode).pack(anchor=W)

def click(value):
    myLabel = Label(root,text=value)
    myLabel.pack()

#Radiobutton(root,text='Option1',variable=r,value=1).pack()
#Radiobutton(root,text='Option2',variable=r,value=2).pack()
#Radiobutton(root,text='Option3',variable=r,value=3).pack()

#myLabel = Label(root,text=pizz.get())
#myLabel.pack()

myButton = Button(root,text="Click Me!",command=lambda: click(pizz.get()))
myButton.pack()
root.mainloop()