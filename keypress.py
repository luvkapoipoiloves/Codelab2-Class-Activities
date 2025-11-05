from tkinter import *

# Create a window object
root = Tk()
root.title("Event handling - Key pressed")
root.geometry("200x200")
root.config(bg="#234567")

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)    
    l2.config(text = event.char)
    

# Bind keypress event to handle_keypress()
root.bind("<Key>", handle_keypress)
# Run the event loop
l1 = Label(root, text="Press any key",bg="#234567", fg='white').pack(pady=10)
l2 = Label(root, text="",bg="#234567", fg='white')
l2.pack()

root.mainloop()