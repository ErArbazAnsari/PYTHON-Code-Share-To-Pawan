#Button in Tkinter
from tkinter import *
def hello():
    print("Hello Friend, I am Python")

def name():
    print("Name is Arbaz Ansari")

root=Tk()
root.geometry("633x333")
frame=Frame(root,bg='grey',borderwidth=4,pady=3,padx=3)
frame.pack()
but1=Button(frame,text="Click Me For Hello",bg='yellow',command=hello)
but1.pack()


but2=Button(frame,text="Check Your Name",bg='green',command=name)
but2.pack()
root.mainloop()