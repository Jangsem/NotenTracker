from tkinter import *

cb_strings = ['item 1', 'item 2', 'item 3', 'item 4']

def sel():
   print("You selected the option " + str(var.get()))


root = Tk()
var = StringVar()


for item in cb_strings:
    button = Radiobutton(root, text=item, variable=var, value=item)
    button.pack(anchor=W)
    button.select()

    def bob():
        name = str(var.get())
        print(name)
        new_window = Tk()
        new_window.geometry("250x250")
        new_window.title(name)

        label = Label(new_window, text=name)
        label.pack()
bsp = Button(root, text="moin", command=bob)
bsp.pack()
root.mainloop()