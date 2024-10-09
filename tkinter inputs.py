from tkinter import *
root = Tk()

e = Entry(root)
e.pack()
e.insert(0,'Enter your name: ')

def myClicck():
  hello = 'hello'+ ' ' + e.get()
  myLabel = Label(root,text= hello)
  myLabel.pack()
  
myButton = Button(root,text='enter your name',command=myClicck)
myButton.pack()

root.mainloop()