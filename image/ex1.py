from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("400x400")
root.title("Image Tkinter")
root.iconphoto(False, ImageTk.PhotoImage(file= "Roblox.png"))
topframe = Frame(root, bg ="green", width=400, height=200)
achi_image = Image.open("Roblox.png")

img = ImageTk.PhotoImage(Image.open("Roblox.png"))

label = Label(root,image =img)
label.pack()

root.mainloop()