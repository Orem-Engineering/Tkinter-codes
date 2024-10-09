from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title('Orem image viewer')
root.iconbitmap('favoritelogo.ico')

#creating image
img_1 = ImageTk.PhotoImage(Image.open("1.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("2.jpg"))
img_3 = ImageTk.PhotoImage(Image.open("3.jpg"))
img_4 = ImageTk.PhotoImage(Image.open("4.jpg"))
img_5 = ImageTk.PhotoImage(Image.open("5.jpg"))
img_6 = ImageTk.PhotoImage(Image.open("6.jpg"))
img_7 = ImageTk.PhotoImage(Image.open("7.jpg"))
img_8 = ImageTk.PhotoImage(Image.open("8.jpg"))
img_9 = ImageTk.PhotoImage(Image.open("9.jpg"))
img_10 = ImageTk.PhotoImage(Image.open("10.jpg"))

#image list
image_list = [img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10]

my_label = Label(image=img_1)
my_label.grid(row=0,column=0 ,columnspan=3)


status = Label (root , text='image ' str(image_number)+ 'of ' + str(len(image_list)),bd = 1, relief=SUNKEN,anchor=E)


#control functions 
def forward(image_number):
  global my_label
  global button_forward 
  global button_back
  
  # deleting already existing image
  my_label.grid_forget()
  my_label = Label(image=image_list[image_number-1])
  
  button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
  button_back = Button(root,text="<<",command=lambda:back(image_number-1))
  my_label.grid(row=0,column=0 ,columnspan=3)
  
  #updating status button
  status = Label (root , text='image' + str(image_number)+ 'of ' + str(len(image_list)),bd = 1, relief=SUNKEN,anchor=E)
  status.grid(row=2,column=0,columnspan=3, sticky=W+E)
  
  #disabling forward button upon reaching last image
  if image_number == 10:
    button_forward = Button(root,text=">>",state=DISABLED)
    
  
  
  button_forward.pack(row=1, column = 0)
  button_back.pack(row=1, column = 2)

def back(image_number):
  global my_label
  global button_forward 
  global button_back
  
  # deleting already existing image
  my_label.grid_forget()
  my_label = Label(image=image_list[image_number-1])
  
  #updating status button
  status = Label (root , text='image '+ str(image_number)+ 'of ' + str(len(image_list)),bd = 1, relief=SUNKEN,anchor=E)
  status.grid(row=2,column=0,columnspan=3, sticky=W+E)
  
  # disabling back button when starting to view the image
  if image_number == 1:
    button_forward = Button(root,text=">>",state=DISABLED)
  
  
  button_forward = Button(root,text=">>",command=lambda:forward(image_number+1))
  button_back = Button(root,text="<<",command=lambda:back(image_number-1))
  my_label.grid(row=0,column=0 ,columnspan=3)
  

#control buttons
button_forward = Button(root,text=">>",command=lambda:forward(2))
button_exit = Button(root,text="Exit Programme",command=root.quit)
button_back = Button(root,text="<<", command= back(),state=DISABLED)

button_forward.pack(row=1, column = 0, pady=10)
button_exit.pack(row=1, column = 1)
button_back.pack(row=1, column = 2)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)

root.mainloop()