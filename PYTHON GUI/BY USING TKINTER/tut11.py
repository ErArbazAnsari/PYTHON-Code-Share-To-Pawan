#Project Travals
from tkinter import *
root=Tk()
root.geometry('655x333')
root.title("Arbaz Travels Booking")
Label(root,text="Welcome To Bus Travelling Counter",font="ubuntu 14 bold").grid(column=3)
name=Label(root,text="Enter Name").grid(row=1)
age=Label(root,text="Enter age").grid(row=2)
gender=Label(root,text="Enter Gender").grid(row=3)
paymode=Label(root,text="PayMent Mode").grid(row=4)

enterName=StringVar()
enterage=StringVar()
entergender=StringVar()
entermode=StringVar()
checkbox=IntVar()

NameEntered=Entry(root,textvariable=enterName).grid(row=1, column=2)
AgeEntered=Entry(root,textvariable=enterage).grid(row=2, column=2)
GenderEntered=Entry(root,textvariable=entergender).grid(row=3, column=2)
ModeEntered=Entry(root,textvariable=entermode).grid(row=4, column=2)


# def checkbutton(text="Pleease Accept", checkbox):
#     pass


# checkbutton(text="Please Accept this agrement.",variable=checkbox)
# checkbox.grid(row=7,column=3)
root.mainloop()
