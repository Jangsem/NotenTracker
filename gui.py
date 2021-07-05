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
x = IntVar()
first_window.geometry("500x500")
first_window.title("Notentracker")
label = Label(text="Name:")
label.pack()

def createNote():
    pass

def createFach():
    pass

def wishNote():
    wish_window = Tk()
    wish_window.geometry("200x200")
    wish_window.title("Wunschnote")
    def berechnenNote(wunsch):
        label = Label(wish_window, text=str(filehandler.wish('deutsch', wunsch)))
        label.pack()


    entryWish = Text(wish_window, bg = "#f54275",height= 1, width= 4)
    entryWish.pack()
    button = Button(wish_window, text="berechnen", command=lambda : berechnenNote(float(entryWish.get("1.0", END))))
    button.pack()



entry = Entry()
entry.insert(0, "Max Muster")
entry.pack()

submit_button = Button(text="submit",command= submit)
submit_button.pack()

delete_button = Button(text="delete", command=delete)
delete_button.pack()

def submitFach(name):
    print(name)
    third_window = Tk()
    third_window.geometry("250x250")
    print(name)
    third_window.title(name)

    noten = filehandler.readNoten(name)
    for index in noten:
        label = Label(third_window, text=str(index))
        label.pack()

    entryNote = Entry(third_window, bg = '#f54275')
    entryNote.pack()
    create_button = Button(third_window,text="erstellen", command=createNote)
    create_button.pack()
    wish_button = Button(third_window, text="Wunschnote", command=wishNote)
    wish_button.pack()

def selectFach():
    global x
    print(faecher)
    submitFach('deutsch')
    print(x.get())

def second_window_create():
    global faecher
    global x
    x = IntVar()
    second_window = Tk()
    second_window.geometry('500x500')
    second_window.title("Faecher")

    namelabel = Label(second_window, text=entry.get())
    namelabel.pack()



    faecher = filehandler.readFach()

    radiobuttons = []

    for index in range(len(faecher)):
        radiobuttons.append(Radiobutton(second_window, text=(faecher[index]+ " " + str(filehandler.averageNoten(faecher[index]))),  # adds text to radio buttons
                                  variable=x,  # groups radiobuttoons if they share same variable
                                  value=index  # assigns each radiobutton a different value
                                  ))
        radiobuttons[index].pack()
    radiobuttons[0].select()

    submit_faecher = Button(second_window, text="submit", command=lambda : selectFach())
    submit_faecher.pack()

    entry_fach = Entry(second_window)
    entry_fach.insert(0,"Fach")
    entry_fach.pack()

    create_fach = Button(second_window, text="create", command=createFach)
    create_fach.pack()

    first_window.destroy()



first_window.mainloop()


