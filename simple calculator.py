from tkinter import *
root= Tk()
root.title('Simple Calculator')
root.iconbitmap('favorite logo.ico')
inputs = Entry(root,width=100, borderwidth=5)
inputs.grid(row=0,column=0,columnspan= 3)

#functions
#numbers functions
def click(number):
  current = inputs.get()
  inputs.delete(0,END)
  inputs.insert(0,str(current)+str(number))

# clear function
def clear():
  inputs.delete(0,END)
  
#add function
def add():
  first_number = inputs.get()
  global f_number
  global math
  math ='addition'
  f_number = int(first_number)
  inputs.delete(0,END)
  

# subtract
def subtract():
  first_number = inputs.get()
  global f_number
  global math
  math ='subtract'
  f_number = int(first_number)
  inputs.delete(0,END)
  

# multiplication
def multiplication():
  first_number = inputs.get()
  global f_number
  global math
  math ='multiplication'
  f_number = int(first_number)
  inputs.delete(0,END)
 

# division
def division():
  first_number = inputs.get()
  global f_number
  global math
  math ='division'
  f_number = int(first_number)
  inputs.delete(0,END)
  
#equal functions
def equall():
  second_number = inputs.get()
  inputs.delete(0,END)
  
  if math == 'addition':
    inputs.insert(0,f_number + int(second_number))
    
  if math == 'subtract':
    inputs.insert(0,f_number - int(second_number))
    
  if math == 'multiplication':
    inputs.insert(0,f_number * int(second_number))
    
  if math == 'division':
    inputs.insert(0,f_number / int(second_number))
    
  
  
  
  
  
  
  
#buttons definition
button_0 = Button(root,text='0',padx=40,pady=20,command=lambda:click(0),bg='white',fg='black') 
button_1 = Button(root,text='1',padx=40,pady=20,command=lambda:click(1),bg='white',fg='black')
button_2 = Button(root,text='2',padx=40,pady=20,command=lambda:click(2),bg='white',fg='black')
button_3 = Button(root,text='3',padx=40,pady=20,command=lambda:click(3),bg='white',fg='black')
button_4 = Button(root,text='4',padx=40,pady=20,command=lambda:click(4),bg='white',fg='black')
button_5 = Button(root,text='5',padx=40,pady=20,command=lambda:click(5),bg='white',fg='black')
button_6 = Button(root,text='6',padx=40,pady=20,command=lambda:click(6),bg='white',fg='black')
button_7 = Button(root,text='7',padx=40,pady=20,command=lambda:click(7),bg='white',fg='black')
button_8 = Button(root,text='8',padx=40,pady=20,command=lambda:click(8),bg='white',fg='black')
button_9 = Button(root,text='9',padx=40,pady=20,command=lambda:click(9),bg='white',fg='black')

button_add = Button(root,text='+',padx=39,pady=20,command=add,bg='white',fg='black')
button_clear = Button(root,text='Clear',padx=131,pady=20,command=clear,bg='white',fg='black')
button_equal = Button(root,text='=',padx=139,pady=20,command=equall,bg='white',fg='black')

button_subtract = Button(root,text='-',padx=40,pady=20,command=subtract,bg='white',fg='black')
button_multiplication = Button(root,text='*',padx=40,pady=20,command=multiplication,bg='white',fg='black')
button_division = Button(root,text='/',padx=40,pady=20,command=division,bg='white',fg='black')


#displaying buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=1,columnspan=2)
button_equal.grid(row=5, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_0.grid(row=4, column=0)

button_subtract.grid(row=6, column=0)
button_multiplication.grid(row=6, column=1)
button_division.grid(row=6, column=2)


root.mainloop()