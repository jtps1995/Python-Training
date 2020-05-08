from tkinter import *

root = Tk()

#creating label widget
my_label_1 = Label(root, text="Hello World!").grid(row=0, column=0)
my_label_2 = Label(root, text="My name is Jake Smith").grid(row=1, column=2)

# placing in a point in the box using .grid dont have to do
# in 2 steps if you dont want to



root.mainloop()
