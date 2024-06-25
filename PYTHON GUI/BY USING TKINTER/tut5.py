from tkinter import *
root=Tk()

root.geometry("733x434")
root.minsize(733,434)
root.maxsize(900,600)
myName=Label(text="My Name is Arbaz Ansari.")
myName.pack()
myPhoto=PhotoImage(file="1.png")
arbaz=Label(image=myPhoto)
arbaz.pack()
root.mainloop()