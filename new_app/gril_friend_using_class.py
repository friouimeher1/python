from tkinter import *
from tkinter import ttk

class Gril():

	def __init__(self,master):

		self.number_gril_friend=3

		self.status_label=ttk.Label(master,text="the number of gril friend : {}".format(str(self.number_gril_friend)),foreground='blue')
		self.button_add_gril_friend=ttk.Button(master,text="Add gril friend",command=self.add_gril)
		self.button_remove_gril_friend=ttk.Button(master,text="Remove Gril Friend",command=self.remove_gril)
		self.status_label.pack()
		self.button_add_gril_friend.pack()
		self.button_remove_gril_friend.pack()

	def add_gril(self):
		self.number_gril_friend +=1
		self.status_label['text']=("the number of gril friend : {}".format(str(self.number_gril_friend)))


	def remove_gril(self):
		self.number_gril_friend -=1
		if(self.number_gril_friend)>0:
			self.status_label['text']=("the number of gril friend : {}".format(str(self.number_gril_friend)))

	def update_label():
				pass		

def main():
	root=Tk()
	root.title('Numbre of gril friend')
	root.geometry('500x500+300+200')
	g=Gril(root)
	root.mainloop()

if __name__=='__main__':
	main()




		
