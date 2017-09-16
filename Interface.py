



from tkinter import *



root =Tk()

root.geometry('700x500+400+200')

root.title('Application python using tkinter')

label =Label(root,text='Age')

label.grid(row=0)

label =Label(root,text='Name')

label.grid(row=1)

label =Label(root,text='Day Alive')

label.grid(row=0,column=3)

entre1=Entry(root)

entre2=Entry(root)

entre1.grid(row=0,column=1)

entre2.grid(row=1,column=1)

button=Button(root,text="Calcul a Live Day")

button.grid(row=3,column=1)

root.mainloop()