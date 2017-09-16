

# f=open(r'/home/meher-frioui/Bureau/AppprendrePython/cool.txt','w')
# for i in range(10):
#     line= ('{} - {} \n'.format(i,i**2))
#     f.write(line)
# f.close()

# f=open(r'/home/meher-frioui/Bureau/AppprendrePython/cool.txt','r')

# for i in f:
#     l=i.replace('-',',')
#     print(l)
# f.close()

# def f(*t):
#     print(t)

# f(1,2,3,3,4,5,6,7,8,9)



# def d(**t):
#     print (t)

# print(d(nom='meher',prénom="FRIOUI",age=26))

# from tkinter import *

# root = Tk()

# def window(main):
#     main.title('First Application')
#     main.geometry('700x500+400+100')

#     label=Label(main,text="Bom Hello World ")
#     label.pack()

#     button =Button(main,text="Click Me Please")
    
#     button.pack()

# window(root)

#root.mainloop()


import application

x=2
def f():
    print(x)

f()
application.f()
print(application.x)