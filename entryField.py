from tkinter import *

root = Tk()

# 'Entry' function creates a field to input data into
entryField = Entry(root, width=50, borderwidth=10, bg="black", fg="white")
entryField.pack()
# 'insert' function allows you to place text inside of entry field
entryField.insert(0, 'Enter Your Name')

# 'get' funtion allows you to get the information from the field
entryField.get()

# gets the information from entry field and displays it upon click
def myClick():
	hello = "Hello " + entryField.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()

myButton = Button(root, text="Enter Your Name", pady=10, padx=10, command=myClick, fg="black", bg="white")
myButton.pack()

root.mainloop()
