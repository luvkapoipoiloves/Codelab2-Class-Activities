from tkinter import *
import tkinter.messagebox
 
root = Tk()
root.title('Tkinter_Program')
root.geometry('400x400')
root.config(bg='#234567')
user_name=StringVar()


def onClick(input):
    num1 = float(e1.get())
    num2 = float(e2.get())
    if(input == 1):
        s = f"sum of two numbers is :{num1+num2}"
    elif input==2:
        s = f"Subtraction of two numbers is :{num1 - num2}"
       
    l2.configure(text=s)      

def sum(num1, num2):
      s = f"sum of two numbers is :{num1+num2}"
      l2.configure(text=s)  
      Message.showInfo("Successful",s)



l1 = Label(root, text = "Enter Values",
bg='#234567',fg="white",font=("tahoma",12))
l1.place(x=10, y=20)

e1 = Entry(root,font=("tahoma",12))
e1.place(x=10, y=60)

e2 = Entry(root,font=("tahoma",12))
e2.place(x=200, y=60)


l2 = Label(root, text = "",
bg='#234567',fg="white",font=("tahoma",12))
l2.place(x=10, y=300)

b1 = Button(root, text = "Sum", fg="yellow", bg="#001111"
,font=("tahoma",12),command =lambda: onClick(1))
b1.place(x=40,y=100)

b2 = Button(root, text = "Sub", fg="yellow", bg="#001111"
,font=("tahoma",12),command =lambda: onClick(2))
b2.place(x=40,y=150)

button = Button(root, text = "add", fg="yellow", bg="#001111"
,font=("tahoma",12),command =lambda: sum(4,5))
button.place(x=40,y=240)
root.mainloop()