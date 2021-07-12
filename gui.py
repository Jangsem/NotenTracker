from tkinter import *
from tkinter import messagebox
from FileHandler import FileHandler

filehandler = FileHandler()
def submit():
    username = entry.get()
    if (username == ''):
        messagebox.showerror(title='Fehler', message='Du musst einen Namen eingeben')
        print("Fehler")
    else:
        second_window.show()

def delete():
    entry.delete(0, END)
def falscheingabe():
    messagebox.showinfo()



first_window = Tk()
frame = Frame(first_window)
first_window.geometry("500x500")
first_window.title("Notentracker")
label = Label(text="Name:")
label.pack()

def createNote():
    pass




entry = Entry()
entry.insert(0, "Max Muster")
entry.pack()

class SecondWindow(Tk):

    def __init__(self, screenName=None, baseName=None, className='Tk',
                 useTk=True, sync=False, use=None):
        super().__init__(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
        self.geometry('500x500')
        self.title("Faecher")

        namelabel = Label(self, text=entry.get())
        namelabel.pack()

        faecher = filehandler.readFach()
        for i in range(len(faecher)):
            faecher[i] += " " + str(filehandler.averageNoten(faecher[i]))
        self.var = StringVar()
        self.var.set(faecher[0])

        dropDown = OptionMenu(self, self.var, *faecher)
        dropDown.pack()

        submit_faecher = Button(self, text="submit", command=self.submitFach)
        submit_faecher.pack()

        entry_faecher = Entry(self)
        entry_faecher.insert(0, "Fach")
        entry_faecher.pack()

        def createFach():
            filehandler.writeFach(entry_faecher.get())

        create_fach = Button(self, text="create", command=createFach)
        create_fach.pack()

    def sel(self):
        print(self.var.get())
    def show(self):
        first_window.destroy()

    def submitFach(self):
        print(self.var.get())
        name = str(self.var.get().split(' ')[0])
        third_window = Tk()
        third_window.geometry("250x250")
        third_window.title(name)

        noten = filehandler.readNoten(name)
        for index in noten:
            label = Label(third_window, text=str(index))
            label.pack()

        textarea = Text(third_window, height=2, width=30)
        textarea.pack()
        create_button = Button(third_window, text="erstellen", command=createNote)
        create_button.pack()
        wish_button = Button(third_window, text="Wunschnote", command=wishNote)
        wish_button.pack()
        print(self.var.get())

second_window = SecondWindow()
submit_button = Button(text="submit",command= submit)
submit_button.pack()


def wishNote():
    wish_window = Tk()
    wish_window.geometry("200x200")
    wish_window.title("Wunschnote")
    def berechnenNote(wunsch):
        label = Label(wish_window, text=str(filehandler.wish(second_window.var.get().split()[0], wunsch)))
        label.pack()


    textarea = Text(wish_window, height=1, width=10)
    textarea.pack()
    button = Button(wish_window, text="berechnen", command=lambda : berechnenNote(float(textarea.get("1.0", END))))
    button.pack()


delete_button = Button(text="delete", command=delete)
delete_button.pack()








first_window.mainloop()