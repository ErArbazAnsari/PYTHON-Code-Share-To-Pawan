# Important Label Options
# text - adds text on application
# bg - background
# fg - foreground
# font - set the font style
# font=("ubuntu",10,"bold"))
# font="ubuntu 10 bold"

# padx - x padding
# pady - y padding
# relief - Boder Styling -sunken, raised, groove, ridge

from tkinter import *
root=Tk()
root.title("Labels")
root.geometry("600x300")
root.minsize(200,200)
root.maxsize(800,400)

arbaz=Label(text='''Video provides a powerful way to help you prove your point. \nWhen you click Online Video, you can paste in the embed \ncode for the video you want to add. You can also type a keyword to search onli\nne for the video that best fits your document.
To make your document look \nprofessionally produced, Word provides header, footer, cover page, \nand text box designs that complement e\nach other. For example, you can add a matching cover page, header, and sidebar. \nClick Insert and then choose the elements you want from the different galleries.
''',bg="yellow",padx=40,pady=60,fg="red", font="ubuntu 10 bold", borderwidth=15, relief="ridge")

# arbaz.pack(anchor="se",fill=("x"))
arbaz.pack(side="left",fill=("y"))
root.mainloop()