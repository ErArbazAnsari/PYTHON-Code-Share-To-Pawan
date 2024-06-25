#Tkinter Tutorial
import tkinter 
root=tkinter.Tk()
root.title("This is Arbaz")
root.geometry("200x200")
root.minsize(100,100)
root.maxsize(500,500)
root.maxsize(500, 300)
arbaz = root.Label(text="Hello My name is Arbaz Ansari.")
arbaz.pack()
arbaz = root.Label(text="Here is my mail id = Arbaz.Ansari2606@gmail.com")
arbaz.pack()
arbaz.pack()

root.mainloop()