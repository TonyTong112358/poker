from tkinter import * 
root = Tk()


label1 = Label(text = 1, borderwidth=2, relief="groove")
label2 = Label(text = 3, borderwidth=2, relief="groove")


def increment(widget):

    widget["text"] += 1




# pack
# grid
# place
root.geometry("500x500")
click1 = Button(root, text = "click me to change label1", height = 5, width = 30, command = lambda:increment(label1))
click2 = Button(root, text = "click me to change label2", height = 5, width = 30, command = lambda:increment(label2))

click1.pack()
click2.pack()
label1.pack()
label2.pack()
button3.pack()
root.mainloop()



