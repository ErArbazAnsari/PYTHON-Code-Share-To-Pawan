from tkinter import *
root=Tk()

root.title("Arbaz")
root.geometry("600x300")
# text1=Label(text="This is arbaz ansari my name is arbaz ansari \ni am currently pursuing my b.tech course.",bg="yellow",fg="red")
# text1.pack(fill='x')
f1=Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f1.pack(side="left",fill='y')
l=Label(f1,text="Left Panel PyCharm",bg='yellow',foreground=('red'))
l.pack(pady=100)
f2=Frame(root,bg='grey',borderwidth=3,relief=SUNKEN)
f2.pack(fill='x')
l=Label(f2,text="Welcome To PyCharm Text Editior Software",bg='yellow',foreground='red')
l.pack()

root.mainloop()