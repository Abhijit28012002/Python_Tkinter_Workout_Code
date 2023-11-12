from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Create code')

def open():
    global my_img
    top = Toplevel()
    top.title('Top Windows')
    my_img = ImageTk.PhotoImage(Image.open("Images/chat.png"))
    my_lable = Label(top,image=my_img).pack()
    btn = Button(top,text="Close windows",command=top.destroy).pack()

btn = Button(root,text="Open Second windows",command=open).pack()
root.mainloop()