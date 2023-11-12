from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn To code at Abhijit With AI")
root.iconbitmap("Images/chat.png") # 16 X 16 image

my_img = ImageTk.PhotoImage(Image.open("Images/Avater.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root,text = "Exit Program",command =root.quit)
button_quit.pack()


root.mainloop()
