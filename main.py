from tkinter import *

root = Tk()
label1 = Label(root, text = "hello world ")
label1.grid(row = 0 , column = 0 )
 
label2 = Label(root, text = " world ",fg = "red")
label2.grid(row = 0 , column = 1 )


root.mainloop()


