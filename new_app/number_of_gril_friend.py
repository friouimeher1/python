from tkinter import *
from tkinter import ttk

count_gril_friend=3


def add_gril_friend():
	global count_gril_friend
	count_gril_friend +=1
	status_label['text']=("the number of gril friend {}".format(str(count_gril_friend)))

def remove_gril_friend():
	global count_gril_friend
	if count_gril_friend>0:
		count_gril_friend -=1
	status_label['text']=("the number of gril friend {}".format(str(count_gril_friend)))


master=Tk()

master.title('courour de copine')


status_label=ttk.Label(master,text="the number of gril friend {}".format(str(count_gril_friend)))

button_add_gril_friend=ttk.Button(master,text="Add new gril friend",command=add_gril_friend)

button_remove_gril_friend=ttk.Button(master,text="Remove new gril friend",command=remove_gril_friend)

status_label.pack()

button_add_gril_friend.pack()

button_remove_gril_friend.pack()

master.mainloop()
