from tkinter import *

root = Tk()
root.title("Arbaz")
# geometry() function working to application size widthxheight
root.geometry("400x200")

# width, height
root.minsize(100, 100)

# width, height
root.maxsize(500, 300)
arbaz=Label(text="Hello My name is Arbaz Ansari.")
arbaz.pack()
arbaz=Label(text="Here is my mail id = Arbaz.Ansari2606@gmail.com")
arbaz.pack()

root.mainloop()
