from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Learn To Create code')

root.filename =filedialog.askopenfilename(initialdir="./Images",title="Select a file",filetypes=(("png files","*.png"),("All files","*.*")))

root.mainloop()