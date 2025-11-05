from tkinter import *


def switch_to_frame(frame):
    frame.tkraise()

# Function to display the greeting
def display_greeting():
    name = entry1.get()
    name2.config(text=f"Hello, {name}! ")
    switch_to_frame(frame2)   


root = Tk()
root.config(bg="#FFFFFF")
root.title("Multiple Frames Example")
root.geometry('400x400')

label_title = Label(root, text="Working with multiple frames", font=('Roboto',18), bg='#FFFFFF',fg='#234567')
label_title.place(x=40, y=0)

# Create Frame 1
frame1 = Frame(root,bg="#234567")

label1 = Label(frame1, text="This is Frame 1", font=('Roboto',16),bg= '#234567', fg='#ffffff')
label1.pack(pady=5)
name1 = Label(frame1, text="Enter name", font=('Roboto',12),bg= '#234567', fg='#ffffff')
name1.pack(pady=5)
entry1 = Entry(frame1, font=('Roboto',12),bg= '#234567', fg='#ffffff')
entry1.pack(pady=5)
button1 = Button(frame1, text="Switch to Frame 2",fg="#ffffff",bg="#234567", command=display_greeting,width=20,font=('Roboto',12))
button1.pack(pady=10)
frame1.place(x=0,y=50, width=400,height=400)


# Create Frame 2
frame2 = Frame(root, bg="green" )


label2 = Label(frame2, text="This is Frame 2", font=('Roboto',16),bg= 'green', fg='#ffffff')
label2.pack(pady=10)

name2 = Label(frame2, text="", font=('Roboto',12),bg= 'green', fg='#ffffff')
name2.pack(pady=10)

button2 = Button(frame2, text="Switch to Frame 1",fg="#ffffff",bg="#234567", command=lambda: switch_to_frame(frame1))
button2.pack()
frame2.place(x=0,y=50, width=400,height=400)
#frame2.grid_rowconfigure(0,weight=1,pad=400)

# Initially, show Frame 1
switch_to_frame(frame1)


root.mainloop()