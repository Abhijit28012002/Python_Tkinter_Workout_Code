from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Learn To Create code')

def popUp():

# showinfo, showwarning, showerror, askquestion, askokcancle, askyesno
    #messagebox.showinfo("This is my Pop Up", "hello World ")
    #messagebox.showerror("This is my Pop Up", "hello World ")
    response = messagebox.showwarning("This is my Pop Up", "hello World ")
    if response==1:
        Label(root,text="Click Yes!!!").pack()
    else:
        Label(root,text="Click No").pack()



Button(root,text="PopUp",command=popUp).pack()


root.mainloop()