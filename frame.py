from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Create code')

########################################

frame = LabelFrame(root,padx=50,pady=50) # Inside padding
frame.pack(padx=10,pady=10) # Outside padding


b=Button(frame,text='Donot click here')
#b.pack()
b.grid(row=0,column=0)

########################################
root.mainloop()