from tkinter import *
window=Tk()
btn=Button(window, text="This is Button widget", fg='blue')
btn.grid(row=1,column=1)
lable1=Label(window,text="This is arbaz Ansari",font="ubuntu 16 bold")
lable1.grid(row=2,column=1)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()