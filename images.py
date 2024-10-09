from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('orem tkinter images')
#root.iconbitmap('c:/Users/USER/Desktop/TRILLON DOLLARS/WALLPAPERS/favorite logo.ico')

my_image = ImageTk.PhotoImage(Image.open("'c:/Users/USER/Desktop/TRILLON DOLLARS/WALLPAPERS/bugatti.jpg"))
my_label = Label(image=my_image)
my_label.pack()

quit_button = Button(root,text='Exit the programme', command=root.quit)
quit_button.pack()

root.mainloop()