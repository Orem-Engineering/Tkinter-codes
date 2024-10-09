from tkinter import *
root = Tk()
root.title('orem tkinter frame')
#root.iconbitmap('favorite logo.ico')

frame1 = LabelFrame(root,text='frame one',padx=50,pady=5)
frame1.pack(padx=100,pady=89)


frame2 = LabelFrame(root,text='frame one',padx=5,pady=5)
frame2.pack(padx=50,pady=50)


frame3 = LabelFrame(root,text='frame one',padx=5,pady=5)
frame3.pack(padx=10,pady=89)

button = Button(frame1,text='button 1')
button.pack()

button = Button(frame2,text='button 1')
button.pack()
button = Button(frame3,text='button 1')
button.grid(row=1,column=0)
button = Button(frame3,text='button 1')
button.grid(row=0,column=0)

root.mainloop()