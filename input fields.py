from tkinter import *
root = Tk()
#Creating input field
userInput  = Entry(root,width=100,bg='white',fg='black',borderwidth=10)
#Display the field
userInput.pack()


def click():
  hello = 'Hello'+ userInput.get()
  userInput = Label(root,text = hello)
  userInput.pack()
  
buton = Button(root,text = 'Name',command=click)
buton.pack()

root.mainloop()