from tkinter import *
root = Tk()
root.title('Orem Calculator')

#Getting user input
userInput = Entry(root,width=150,bg='white',fg='black',borderwidth=5)
userInput.grid(row= 0,column=0,columnspan=4)

#Logic & functions of the calculator
def addition():
  return 0
def subtraction():
  return 0

def multiplication():
  return 0

def division():
  return 0

def equal():
  return 0

def clear():
  return 0

#Creating buttons
button1 = Label(root,text='1',bg='white',fg='black',padx= 40,pady=20)
button2 = Label(root,text='2',bg='white',fg='black',padx= 40,pady=20)
button3 = Label(root,text='3',bg='white',fg='black',padx= 40,pady=20)
button4 = Label(root,text='4',bg='white',fg='black',padx= 40,pady=20)
button5 = Label(root,text='5',bg='white',fg='black',padx= 40,pady=20)
button6 = Label(root,text='6',bg='white',fg='black',padx= 40,pady=20)
button7 = Label(root,text='7',bg='white',fg='black',padx= 40,pady=20)
button8 = Label(root,text='8',bg='white',fg='black',padx= 40,pady=20)
button9 = Label(root,text='9',bg='white',fg='black',padx= 40,pady=20)
button0 = Label(root,text='0',bg='white',fg='black',padx= 40,pady=20)

#Logic functions
additionButton = Label(root,text='+',bg='white',fg='black',padx= 40,pady=20)
subtractionButton = Label(root,text='-',bg='white',fg='black',padx= 40,pady=20)
multiplicationButton = Label(root,text='*',bg='white',fg='black',padx= 40,pady=20)
divisionButton= Label(root,text='/',bg='white',fg='black',padx= 40,pady=20)
equallButton = Label(root,text='=',bg='white',fg='black',padx= 40,pady=20)
clearButton = Label(root,text='clear',bg='white',fg='black',padx= 40,pady=20)

#displaying buttons
button0.grid(row= 4,column= 0,columnspan=2 )

button1.grid(row=3 ,column=0 )
button2.grid(row=3 ,column=1)
button3.grid(row= 3,column= 2)

button4.grid(row=2 ,column= 0)
button5.grid(row=2 ,column= 1)
button6.grid(row=2 ,column= 2)
button7.grid(row=1 ,column=0 )

button8.grid(row=1 ,column=1 )
button9.grid(row=1 ,column= 2)
additionButton.grid(row=4 ,column=2 )
multiplicationButton.grid(row=2 ,column=3)

divisionButton.grid(row=1,column=3)
clearButton.grid(row=1 ,column=5 )
subtractionButton.grid(row=3 ,column=3 )
equallButton.grid(row=3 , columnspan=2, column= 4 )

root.mainloop()