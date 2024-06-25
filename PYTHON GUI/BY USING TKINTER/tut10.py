from tkinter import *
root=Tk()
def getvalues():
    print(f"The user name is {userentry.get()}")
    print(f"The user password is {passentry.get()}")
# root.state('zoomed')
root.minsize(400,400)
root.title("Arbaz Software Windows")

username=Label(root,text='Enter UserName')
username.grid(row=0)
userPass=Label(root,text='Enter UserPass')
userPass.grid(row=1)

enteruser=StringVar()
enterpass=StringVar()

userentry=Entry(root,textvariable=enteruser)
passentry=Entry(root,textvariable=enterpass)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(root,text='Submit',command=getvalues).grid()
root.mainloop()