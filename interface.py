from tkinter import *

root = Tk()

root.title('Application using tkinter python')

root.geometry('700x500+300+200')

label = Label(root,text="Value 1")
label.pack()

label['text']="very nice"


button =Button(root,text="Click me")
button.pack()

enter =Entry(root)
enter.pack()

root.mainloop()