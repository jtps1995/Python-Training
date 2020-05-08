from tkinter import *

root = Tk()

#creating label widget
my_label_1 = Label(root, text="Hello World!")
my_label_2 = Label(root, text="My name is Jake Smith")
my_label_3 = Label(root, text= "             ")

# placing in a point in the box using .grid
my_label_1.grid(row=0, column=0)
my_label_2.grid(row=1, column=2)
#using my_label_3 to seperate the 2 as 
#they are relative to eachother without this line
my_label_3.grid(row=1, column=1)

root.mainloop()
