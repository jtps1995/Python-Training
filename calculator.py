from tkinter import *

root = Tk()
#'Title' function changes the name in the toolbar at top of window
root.title("Calculator")

entryField = Entry(root, width=35, borderwidth=5)
# columnspan refers to how many columns field will span over
entryField.grid(row=0,column=0, columnspan=3, padx=10,pady=10)

def button_click(number): # defining what happens when number button is clicked
	#entryField.delete(0,END) # deleting information in entry field when clicked before inserting next number
	current = entryField.get() # gets and keeps the number previously inserted
	entryField.delete(0,END)
	entryField.insert(0, str(current) + str(number)) # inserts the number into the field
	# creating the current variable allows us to place the information before the new info
	# also need to make sure these are strings or else they would just add numerically
	# this is done by using the string function 'str()'

def button_clear(): # defining what happens when clear button is clicked
	entryField.delete(0,END)


def button_add(): # defining what the add button click will do
	first_number = entryField.get()
	# need the calculator to remember the number previously input using a global variable
	global f_num # global means we can use it outside of this function
	global math
	math = "addition"
	f_num = int(first_number) #int() makes the information a integer number
	entryField.delete(0,END) # need to delete previously inserted number
	# need it to then perform add

def button_eql(): # defining what clicking button = does
	second_number = entryField.get() # retrieves the 2nd number
	entryField.delete(0,END) # clears the entry field
	#entryField.insert(0,f_num + int(second_number)) # inserts the sum

	if math == "addition":
		entryField.insert(0,f_num + int(second_number))
		# when looking at global if it reads addition then will add

	if math == "subtraction":
		entryField.insert(0,f_num - int(second_number))
		# when looking at global if it reads subtraction then will minus

	if math == "multiplication":
		entryField.insert(0,f_num * int(second_number))
		# when looking at global if it reads multiplication then will multiply
	if math == "division":
		entryField.insert(0,f_num / int(second_number))
		# when looking at global if it reads division then will divide

def button_subtract():
	first_number = entryField.get()
	# need the calculator to remember the number previously input using a global variable
	global f_num # global means we can use it outside of this function
	global math
	math = "subtraction"
	f_num = int(first_number) #int() makes the information a integer number
	entryField.delete(0,END) # need to delete previously inserted number
	# need it to then perform add

def button_multiply():
	first_number = entryField.get()
	# need the calculator to remember the number previously input using a global variable
	global f_num # global means we can use it outside of this function
	global math
	math = "multiplication"
	f_num = int(first_number) #int() makes the information a integer number
	entryField.delete(0,END) # need to delete previously inserted number
	# need it to then perform add

def button_div():
	first_number = entryField.get()
	# need the calculator to remember the number previously input using a global variable
	global f_num # global means we can use it outside of this function
	global math
	math = "division"
	f_num = int(first_number) #int() makes the information a integer number
	entryField.delete(0,END) # need to delete previously inserted number
	# need it to then perform add

#defineing buttons

#lambda function allows us to pass variable through the command
#as button_click covers multiple nummbers this function is needed or
# you could create multipls def button clicks for each number
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
# lambda function not needed as button_add is not changing just a singular function
button_clr = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
# lambda function not needed as button_clear is not changing nor are ()
button_eql = Button(root, text="=", padx=91, pady=20, command=button_eql) 

button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
button_div = Button(root, text="/", padx=40, pady=20, command=button_div)


# placing buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clr.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_eql.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()