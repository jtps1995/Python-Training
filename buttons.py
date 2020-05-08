from tkinter import *

root = Tk()

#creating a funtion by using define (def), effect of clicking the button
# use the : after the myclick definintion
def myClick():
	myLabel = Label(root, text="Look I clicked a button!!")
	myLabel.pack()

#line 15 notation:
#creating button 'pad(x or y)' adds padding to the button
#command function actually tells computer what to do when clicked
# don't include () on the command on myClick function in button function
#or it won't work
# fg is forground colour, bg is background
# can use hex colour format ie #ffffff

myButton = Button(root, text="Click Me", pady=50, padx=10, command=myClick, fg="red", bg="blue")
#placing button
myButton.pack()

root.mainloop()
