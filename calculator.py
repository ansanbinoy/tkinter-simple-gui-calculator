__author__ = "ansanbinoy"

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
os.system('clear')

class Calc:
	def __init__(self, app):
		self.calc = ''
		app.resizable(0,0)
		app.title('Clculator')
		frame1 = Frame(app)
		frame2 = Frame(app)
		frame3 = Frame(app)
		frame1.pack(side=TOP, fill=X)
		frame2.pack(side=TOP, fill=X)
		frame3.pack(side=BOTTOM, fill=X)
		self.mainText = Text(frame1, width=33, height=4, state='normal')
		self.mainText.grid(row=0, column=0)
#		Clear Button.
		self.clear = ttk.Button(frame2, text='C', width=7, command=self.clear_)
		self.clear.grid(row=2, column=0)
#		Number Buttons.
		self.button0 = ttk.Button(frame3, text='0', width=15,command=lambda : self.keyPress('0')).grid(row=6, column=0)
		self.button9 = ttk.Button(frame3, text='.', width=7, command=lambda : self.keyPress('.')).grid(row=6, column=1)
		self.equal = ttk.Button(frame3, text='=', width=7, command=self.equal_).grid(row=6, column=2)
		self.button1 = ttk.Button(frame2, text='1', width=7, command=lambda : self.keyPress('1')).grid(row=5, column=0)
		self.button2 = ttk.Button(frame2, text='2', width=7, command=lambda : self.keyPress('2')).grid(row=5, column=1)
		self.button3 = ttk.Button(frame2, text='3', width=7, command=lambda : self.keyPress('3')).grid(row=5, column=2)
		self.button4 = ttk.Button(frame2, text='4', width=7, command=lambda : self.keyPress('4')).grid(row=4, column=0)
		self.button5 = ttk.Button(frame2, text='5', width=7, command=lambda : self.keyPress('5')).grid(row=4, column=1)
		self.button6 = ttk.Button(frame2, text='6', width=7, command=lambda : self.keyPress('6')).grid(row=4, column=2)
		self.button7 = ttk.Button(frame2, text='7', width=7, command=lambda : self.keyPress('7')).grid(row=3, column=0)
		self.button8 = ttk.Button(frame2, text='8', width=7, command=lambda : self.keyPress('8')).grid(row=3, column=1)
		self.button9 = ttk.Button(frame2, text='9', width=7, command=lambda : self.keyPress('9')).grid(row=3, column=2)
		self.buttonAdd = ttk.Button(frame2, text='+', width=7, command=lambda : self.keyPress('+')).grid(row=5, column=3)
		self.buttonMinus = ttk.Button(frame2, text='—', width=7, command=lambda : self.keyPress('-')).grid(row=4, column=3)
		self.buttonDivide = ttk.Button(frame2, text='÷', width=7, command=lambda : self.keyPress('/', '÷')).grid(row=3, column=3)
		self.buttonMultyply = ttk.Button(frame2, text='x', width=7, command=lambda: self.keyPress('*', 'x')).grid(row=2,column=3)
		self.none = ttk.Button(frame2, text='Exit', width=7, command=lambda : app.destroy()).grid(row=2, column=1)
		self.back = ttk.Button(frame2, text='⌫', width=7, command=self.back_).grid(row=2,column=2)
		#		Number Buttons Placements.

		# self.mainText.focus()

	def clear_(self):
		self.mainText.delete('1.0','end')
		self.calc = ''
		# self.mainText.focus()

	def keyPress(self,val, sval=None):
		self.calc += val
		if sval != None:
			self.mainText.insert('1.0 + 2 lines', sval)
		else:
			self.mainText.insert('1.0 + 2 lines', val)
	def equal_(self):
		try:
			res = eval(self.calc)
			self.mainText.insert(END,f'\n\n\n\t{res}')
		except:
			messagebox.showerror('Try again', 'Somthing went wrong!!')

	def back_(self):
		string = self.mainText.get('1.0', '1.end')
		index = len(string) -1
		self.mainText.delete(f'1.{index}', 'end')
		scind = len(self.calc) -1
		self.calc = self.calc[:scind]

def main():
	app = Tk()
	Calc(app)
	app.mainloop()

if __name__ == '__main__':
	main()
