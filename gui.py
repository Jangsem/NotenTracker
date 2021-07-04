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
        second_window_create()


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

def wishNote():
    wish_window = Tk()
    wish_window.geometry("200x200")
    wish_window.title("Wunschnote")
    def berechnenNote(wunsch):
        label = Label(wish_window, text=str(filehandler.wish('informatik', wunsch)))
        label.pack()


    textarea = Text(wish_window, height=1, width=10)
    textarea.pack()
    button = Button(wish_window, text="berechnen", command=lambda : berechnenNote(float(textarea.get("1.0", END))))
    button.pack()



entry = Entry()
entry.insert(0, "Max Muster")
entry.pack()

submit_button = Button(text="submit",command= submit)
submit_button.pack()

delete_button = Button(text="delete", command=delete)
delete_button.pack()

def submitFach(name):
    third_window = Tk()
    third_window.geometry("250x250")
    third_window.title(name)

    noten = filehandler.readNoten(name)
    for index in noten:
        label = Label(third_window, text=str(index))
        label.pack()

    textarea = Text(third_window, height=2, width=30)
    textarea.pack()
    create_button = Button(third_window,text="erstellen", command=createNote)

    wish_button = Button(third_window, text="Wunschnote", command=wishNote)
    wish_button.pack()


def second_window_create():
    second_window = Tk()
    second_window.geometry('500x500')
    second_window.title("Faecher")

    namelabel = Label(second_window, text=entry.get())
    namelabel.pack()



    faecher = filehandler.readFach()

    x = IntVar()

    for index in range(len(faecher)):
        radiobutton = Radiobutton(second_window, text=(faecher[index]+ " " + str(filehandler.averageNoten(faecher[index]))),  # adds text to radio buttons
                                  variable=x,  # groups radiobuttoons if they share same variable
                                  value=index  # assigns each radiobutton a different value
                                  )
        radiobutton.pack()
    radiobutton.select()

    submit_faecher = Button(second_window, text="submit", command=lambda : submitFach(faecher[index]))
    submit_faecher.pack()

    first_window.destroy()



first_window.mainloop()


