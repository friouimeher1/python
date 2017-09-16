from tkinter import *
from tkinter import *




class Gril():

	def __init__(self,root):
		
		self.label =ttk.Label(root,text="Number of gril friend")

		self.button_add_gril_friend=ttk.Button(root,text="add new gril friend")

		self.button_remove_gril_friend=ttk.Button(root,text="remove gril friend")

		self.label.pack()

		self.button_add_gril_friend.pack()

		self.button_remove_gril_friend.pack()



def main():

	master=Tk()
	master.title('The number of gril friend')
	mster.geometry('300x300+500+300')
	a=Gril(master)


	if __name__ == '__main__':

		main()