from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('Images/letter.png')

my_img1 = ImageTk.PhotoImage(Image.open("Images/letter.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/cloud.png"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/deletefile.png"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/heavyrain.png"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/penguin.png"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

# Add status bar
status = Label(root, text="Image 1 to 5")


my_label = Label(image = my_img1)
my_label.grid(row=0,column=0, columnspan=3)


def forward(imageNum):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[imageNum-1])
    button_forward = Button(root,text=">>",command=lambda: forward(imageNum+1))
    button_back = Button(root,text="<<",command=lambda: back(imageNum-1))
    
    if imageNum ==5 :
        button_forward= Button(root,text=">>",state=DISABLED)

    
    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1, column=2)

def back(imageNum):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[imageNum-1])
    button_forward = Button(root,text=">>",command=lambda: forward(imageNum+1))
    button_back = Button(root,text="<<",command=lambda: back(imageNum-1))
    
    if imageNum == 1:
        button_back=Button(root,text="<<",state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back,state=DISABLED)
button_exit = Button(root,text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
