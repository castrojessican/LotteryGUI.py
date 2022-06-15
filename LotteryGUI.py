"""
Program: LotteryGUI.py (page 251)
Author: Jessica 6/14/2022

GUI-based app to simulate the Mega Millions lottery number picks. Five random numbers between 1 and 70 
and a "Mega Ball" between 1 and 25..
"""

from breezypythongui import EasyFrame
from tkinter.font 	import Font 
import random 
# other imports

class Lottery(EasyFrame):
	# "ApplicationName" will change from project to project

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# Call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Mega Millions Draw", background = "pink")
		bigFont = Font(family = "Verdana", size = 32, weight = "bold")
		self.addLabel(text = "Mega Millions", row = 0, column = 0, columnspan = 5,
		background = "pink", foreground = "royal blue", font = bigFont)
		self.addLabel(text = "MEGA MILLIONS JACKPOT", row = 0, column = 0, columnspan = 3,
		background = "pink", foreground = "royal blue", sticky = "NSEW")
		# Load the image into an imageLabel object
		self.addLabel(text = "Winning Number", row = 0, column = 0, background = "pink", foreground = "white")
		self.field1 = self.addIntegerField(value = 0, row = 2, column = 0, state = "readonly")
		self.field2 = self.addIntegerField(value = 1, row = 2, column = 1, state = "readonly")
		self.field3 = self.addIntegerField(value = 2, row = 2, column = 2, state = "readonly")
		self.field4 = self.addIntegerField(value = 3, row = 2, column = 3, state = "readonly")
		self.field5 = self.addIntegerField(value = 4, row = 2, column = 4, state = "readonly")
		self.addLabel(text = "Mega Ball", row = 3, column= 0, columnspan = 5, sticky ="NSEW", background = "pink",
		foreground = "white")
		self.megafield = self.addIntegerField(value = 0, row = 4, column = 0, columnspan = 5, sticky = "NSEW")
		self.megafield["background"] = "pink"
		self.addButton(text = "Draw Numbers", row = 5, column = 0, columnspan = 5, command = self.drawNumbers)

# Event handling method for the button
def drawNumbers(self):
	num1 = random.randint(1,70)
	num2 = random.randint(1,70)
	num3 = random.randint(1,70)
	num4 = random.randint(1,70)
	num5 = random.randint(1,70)
	mega = random.randint(1,25)

	self.field1.setNumber(num1)
	self.field2.setNumber(num2)
	self.field3.setNumber(num3)
	self.field4.setNumber(num4)
	self.field5.setNumber(num5)
	self.megafield.setNumber(mega)


# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into the mainloop()
	Lottery().mainloop()

# global call to the main() method
main()