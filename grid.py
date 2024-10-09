from tkinter import *
root = Tk()
#creating label widget
myLabel1 = Label(root,text='This is tkinter project')
myLabel2 = Label(root,text='Hello world')
myLabel3 = Label(root,text='trillion D            ')
myLabel5 = Label(root,text='                                                                                  ').grid(row= 4,column=0)
myLabel4 = Label(root,text='orem babu')
#shoving it to screen
myLabel1.grid(row =0,column = 0)
myLabel2.grid(row=1, column= 3 )
myLabel3.grid(row=2,column = 0)
myLabel4.grid(row=6,column=0)
#loop to figure mouse position
root.mainloop()